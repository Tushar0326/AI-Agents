# 📰 ➡️ 🎙️ Blog to Podcast Agent

A small Streamlit app that scrapes a blog post, generates a concise podcast-style summary using OpenAI, and converts the summary to spoken audio via ElevenLabs.

---

## 🚀 Features
- Scrapes a public blog URL and summarizes it for podcast-style narration
- Uses OpenAI for summarization and ElevenLabs for text-to-speech
- Simple Streamlit UI with sidebar for API keys and a main input for the blog URL

---

## ⚙️ Requirements
- Python 3.10+ (recommended)
- Streamlit
- See `requirements.txt` for full dependency list

---

## ✅ Quickstart
1. Clone / open this project folder.
2. Create and activate a virtual environment (Windows PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Provide your API keys:
- You can enter them in the app sidebar (runtime input).
- Or create a `.env` file in the project root with the following keys (optional):

```
OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=your_elevenlabs_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

> Note: The app currently asks for keys in the sidebar. If you prefer to set environment variables in PowerShell for a session, run:
>
> $env:OPENAI_API_KEY = "sk-..."
> $env:ELEVENLABS_API_KEY = "..."
> $env:FIRECRAWL_API_KEY = "..."

4. Run the app (two options):
- If your filename contains spaces, quote the path:

```powershell
streamlit run ".\blog to podcast agent.py"
```

- Or rename the file to remove spaces (recommended):

```powershell
Rename-Item "blog to podcast agent.py" "blog_to_podcast_agent.py"
streamlit run .\blog_to_podcast_agent.py
```

---

## 🧭 How to use the app
1. Open the Streamlit app in your browser.
2. In the **sidebar**, paste your **OpenAI**, **ElevenLabs**, and **Firecrawl** API keys.
3. In the main page, paste a public blog URL (e.g., a fully-qualified `https://...` URL).
4. Click **🎙️ Generate Podcast**. The app will scrape the blog, produce a summary, generate audio, and show a player plus a download button.

---

## 🔧 Troubleshooting
- Streamlit shows an error about a file with no extension: Quote the filename with spaces or rename the file (see Quickstart).
- "Fill all API keys" / Generate button not working: Make sure all required API keys are provided in the sidebar; the app shows which keys are missing.
- If audio generation fails, check your ElevenLabs key and model/voice IDs; review the Streamlit error message shown in-app.
- If scraping fails, ensure the target URL is publicly accessible and not blocked by robots or rate limits.

---

## 🧪 Testing
- Use a simple public blog post URL for testing.
- If you want a reproducible setup, add keys to `.env` and export them into your session before launching Streamlit.

---

## 🛠️ Contributing
Contributions are welcome. Open an issue or submit a PR if you want to:
- Improve scraping robustness
- Add caching or progress indicators
- Add automated tests or CI

---

## 📄 License
This project has no license specified. Add a LICENSE file if you want to open-source it under a standard license.

---



