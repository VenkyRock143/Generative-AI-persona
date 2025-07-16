# 🧠 Reddit User Persona Generator

Generate a detailed, research-style user persona from any Reddit user's **public posts and comments** using OpenAI GPT-4 and Reddit API.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-black?style=flat-square&logo=openai)
![Reddit](https://img.shields.io/badge/Reddit-API-orange?style=flat-square&logo=reddit)

---

## 📌 Features

- 🔍 Takes Reddit profile URL or username as input
- 🧵 Scrapes recent posts and comments (up to 70 total)
- 🧑‍💼 Builds a structured **User Persona**
- 📝 Cites Reddit content (posts/comments) used for each insight
- 📄 Saves output as `.txt` file (e.g., `kojied_persona.txt`)

---

## 🚀Command

```bash
python main.py https://www.reddit.com/user/kojied/
🛠️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/VenkyRock143/Generative-AI-persona.git

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Setup .env File
Create a .env file using the template below:
.env
OPENAI_API_KEY=your_openai_key_here
REDDIT_CLIENT_ID=your_reddit_app_id
REDDIT_CLIENT_SECRET=your_reddit_app_secret
USER_AGENT=reddit-persona-script/0.1 by your_reddit_username
💡 You can get these keys from:

OpenAI: https://platform.openai.com/account/api-keys

Reddit API: https://www.reddit.com/prefs/apps

🔄 Run the Script
python main.py <reddit_username_or_url>
Example:
python main.py Hungry-Move-6603

📁 Output
Each run creates a .txt file in the same folder, named:
<username>_persona.txt
Example:
kojied_persona.txt
hungry_move_6603_persona.txt

