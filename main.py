import logging

from dotenv import load_dotenv

from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    cli,
    metrics,
    room_io,
)
from livekit.plugins import silero, rime, gladia, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("rime-gladia-agent")

load_dotenv()


class MyAgent(Agent):
    """Voice assistant agent for the Rime + Gladia demo."""

    def __init__(self) -> None:
        super().__init__(
            instructions="You're a friendly voice assistant demoing Rime TTS and Gladia STT. Keep responses short and conversational—like chatting with a friend. No emojis, no markdown, just natural speech. Be warm, helpful, and don't over-explain."
        )

    async def on_enter(self) -> None:
        """Greet the user when the agent joins the session."""
        self.session.say(
            "Hey there! I'm your voice assistant, powered by Rime and Gladia. Feel free to chat with me about anything. I'm here to help!"
        )


server = AgentServer()


def prewarm(proc: JobProcess) -> None:
    """Load the Silero VAD model before handling requests."""
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm


@server.rtc_session()
async def entrypoint(ctx: JobContext) -> None:
    """
    Main session handler for the voice agent.

    Sets up Gladia STT, Rime TTS, OpenAI LLM, and noise cancellation.
    """
    ctx.log_context_fields = {"room": ctx.room.name}

    session = AgentSession(
        stt=gladia.STT(),
        llm="openai/gpt-4o",
        tts=rime.TTS(model="arcana", speaker="oculus"),
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
    )

    # log metrics as they are emitted, and total usage after session is over
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage() -> None:
        """Log usage metrics when the session ends."""
        summary = usage_collector.get_summary()
        logger.info("Usage: %s", summary)

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        agent=MyAgent(),
        room=ctx.room,
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=noise_cancellation.BVC(),
            ),
        ),
    )


if __name__ == "__main__":
    cli.run_app(server)
