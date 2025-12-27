import os
from uuid import uuid4
from dotenv import load_dotenv

from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat
from agno.tools.firecrawl import FirecrawlTools
from elevenlabs import ElevenLabs
import streamlit as st

# --------------------------------------------------
# Load .env
# --------------------------------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# --------------------------------------------------
# Streamlit Setup
# --------------------------------------------------
st.set_page_config(page_title="📰 ➡️ 🎙️ Blog to Podcast", page_icon="🎙️")
st.title("📰 ➡️ 🎙️ Blog to Podcast Agent")

# --------------------------------------------------
# Validate API Keys
# --------------------------------------------------
missing_keys = []
if not OPENAI_API_KEY:
    missing_keys.append("OPENAI_API_KEY")
if not ELEVENLABS_API_KEY:
    missing_keys.append("ELEVENLABS_API_KEY")
if not FIRECRAWL_API_KEY:
    missing_keys.append("FIRECRAWL_API_KEY")

if missing_keys:
    st.error(
        f"❌ Missing API keys in `.env`: {', '.join(missing_keys)}\n\n"
        "Please add them to your `.env` file and restart the app."
    )
    st.stop()
else:
    st.success("✅ API keys loaded from .env")

# --------------------------------------------------
# Blog URL Input
# --------------------------------------------------
url = st.text_input(
    "Enter Blog URL:",
    placeholder="https://example.com/blog-post"
)

# --------------------------------------------------
# Generate Podcast
# --------------------------------------------------
if st.button("🎙️ Generate Podcast"):
    if not url.strip():
        st.warning("Please enter a blog URL")
    else:
        with st.spinner("Scraping blog and generating podcast..."):
            try:
                # Set env vars explicitly (safe for libraries)
                os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
                os.environ["FIRECRAWL_API_KEY"] = FIRECRAWL_API_KEY

                agent = Agent(
                    name="Blog Summarizer",
                    model=OpenAIChat(id="gpt-4o"),
                    tools=[FirecrawlTools()],
                    instructions=[
                        "Scrape the blog URL and create a concise, engaging summary (max 2000 characters) suitable for a podcast.",
                        "The summary should be conversational and capture the main points."
                    ],
                )

                response: RunOutput = agent.run(
                    f"Scrape and summarize this blog for a podcast: {url}"
                )

                summary = response.content if hasattr(response, "content") else str(response)

                if not summary:
                    st.error("Failed to generate summary")
                    st.stop()

                # ElevenLabs TTS
                client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
                audio_generator = client.text_to_speech.convert(
                    text=summary,
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                    model_id="eleven_multilingual_v2"
                )

                audio_bytes = b"".join(chunk for chunk in audio_generator if chunk)

                st.success("🎧 Podcast generated successfully!")
                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    "⬇️ Download Podcast",
                    audio_bytes,
                    "podcast.mp3",
                    "audio/mp3"
                )

                with st.expander("📄 Podcast Summary"):
                    st.write(summary)

            except Exception as e:
                st.error(f"Error: {e}")
