# Rime-Gladia Voice Assistant

A demonstration of building a voice agent pipeline using **LiveKit Agents**, featuring **Gladia STT** (Speech-to-Text), **OpenAI LLM** (Large Language Model), and **Rime TTS** (Text-to-Speech). This project showcases how to create a seamless voice interaction system with state-of-the-art AI services.

## 🚀 Getting Started

### 1. Clone the Repository

You can clone this repository using either HTTPS or SSH:

```bash
# HTTPS
git clone https://github.com/rimelabs/Rime-gladia.git

# SSH
git clone git@github.com:rimelabs/Rime-gladia.git

cd Rime-gladia
```

### 2. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add the following API keys to your `.env` file:

```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=wss://your-project.livekit.cloud

RIME_API_KEY=your_rime_api_key
OPENAI_API_KEY=your_openai_api_key
GLADIA_API_KEY=your_gladia_api_key
```

> **⚠️ Note:** All API keys are required for this application to work flawlessly.

### 3. How to Obtain the API Keys

#### LiveKit API Keys
1. Sign up or log in at [LiveKit Cloud](https://cloud.livekit.io/login)
2. Navigate to **Settings → API Keys**
3. Generate your API key and secret
4. Copy your project URL (e.g., `wss://your-project.livekit.cloud`)

#### Rime API Key
1. Visit [Rime Tokens](https://app.rime.ai/tokens/)
2. Sign in to your Rime account
3. Generate an API token

#### OpenAI API Key
1. Sign up or log in at [OpenAI Platform](https://platform.openai.com/settings/organization/api-keys)
2. Navigate to API Keys section
3. Create a new API key

#### Gladia API Key
1. Visit [Gladia API Keys](https://app.gladia.io/apikeys)
2. Sign in to your Gladia account
3. Generate a new API key

### 4. Install Dependencies

This project uses [`uv`](https://github.com/astral-sh/uv) for fast and reliable Python package management.

**Install `uv`** (if not already installed):

```bash
# macOS (using Homebrew)
brew install uv

```

**Install project dependencies:**

```bash
uv sync
```

### 5. Download Required Model Files

This step downloads models for turn detection, Silero VAD, and noise cancellation. **This only needs to be done once:**

```bash
uv run main.py download-files
```

## 🎮 Running the Agent

The agent can be run in three different modes depending on your use case:

### Console Mode 
Run the agent directly in your terminal for quick local testing:
```bash
uv run main.py console
```

This mode simulates voice interaction in the console without requiring a LiveKit room.

### Development Mode 
Connect to LiveKit Cloud for testing over the internet:

**Step 1: Create a Sandbox Environment**

1. Go to [LiveKit Cloud Dashboard](https://cloud.livekit.io/)
2. Navigate to **Sandbox** in the sidebar
3. Choose **Web Voice Agent** as your sandbox type
4. Create a new sandbox

**Step 2: Launch the Sandbox**

1. Under **Sandbox App**, find the sandbox you just created
2. Click the **Launch** button on your sandbox

**Step 3: Start the Agent**

Run the development mode command in your terminal:

```bash
uv run main.py dev
```

**Step 4: Connect to the Agent**

Once the agent is running, click the **Start** button in your sandbox interface to begin voice interaction.

### Production Mode
Run the agent in production environment:

```bash
uv run main.py start
```


