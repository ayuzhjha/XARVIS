# 🤖 XARVIS: Your Personal AI Voice Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![Voice Assistant](https://img.shields.io/badge/AI-XARVIS-success?logo=github)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> 💬 “Good Morning, Boss!” – A voice-activated assistant powered by Python, speech recognition, and LLaMA 2 via [Ollama](https://ollama.com).

---

## 🧠 Features

- ⏰ Dynamic time-based greetings
- 🌤 Real-time weather reports
- 📰 Latest news headlines
- 🧏 Speech recognition (Google API)
- 🔊 Text-to-speech (TTS) using `pyttsx3`
- 🧠 LLaMA 2 chat integration via `ollama`
- ⚙️ Auto-run on Windows startup (optional)

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/ayuzhjha/XARVIS.git
cd XARVIS
```

### 2. Install Dependencies

Make sure Python 3.10+ is installed. Then:

```bash
pip install requests pyttsx3 SpeechRecognition pyaudio ollama
```

> ⚠️ On Windows, install `pyaudio` via a `.whl` if `pip` fails:  
> Download from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## 🔑 API Keys Setup

Replace the placeholders in the script with your actual keys:

```python
weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
news_api_key = "YOUR_NEWSAPI_KEY"
location = "Your City"
```

- Get weather key → [OpenWeatherMap](https://openweathermap.org/api)
- Get news key → [NewsAPI](https://newsapi.org/)

---

## 🧪 How to Use

Run the assistant:

```bash
python main.py
```

- XARVIS will:
  - Greet you based on the time
  - Tell the current time
  - Announce the weather and news
  - Ask: “I am ready to assist you. Please ask me anything.”
- Respond by speaking into your mic.
- Say `"exit"` or `"bye"` to end the session.

---

## ⚙️ Enable Auto-Start on Boot (Optional)

The script uses Windows registry to add itself to startup:

```python
add_to_startup()  # Already called in main
```

To disable it, remove the `"JARVIS"` key manually from:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```

---

## 🧠 Behind the Scenes

| Module         | Role                        |
|----------------|-----------------------------|
| `speech_recognition` | Voice to text            |
| `pyttsx3`      | Text to voice                |
| `ollama`       | Chat interaction via LLaMA 2 |
| `requests`     | Weather + News API calls     |
| `winreg`       | Adds to startup              |

---

## ⚡ Future Upgrades

- [ ] GUI support with PyQt or Tkinter
- [ ] Custom voice personas
- [ ] File search & automation features
- [ ] Voice-controlled system commands

---

## 👨‍💻 Author

Made with ❤️ by **Ayush Jha (A.J.)**  
🛠️ Division: **XAEZOR → XARVIS (AI Assistant)**  
📫 Reach out: [GitHub](https://github.com/ayuzhjha)

---

> 🧬 “Part of XAEZOR – a futuristic ecosystem where intelligence meets automation.”
