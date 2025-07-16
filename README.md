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

## 🚀 Demo Command

```bash
python main.py https://www.reddit.com/user/kojied/
🛠️ Setup Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Setup .env File
Create a .env file using the template below:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
REDDIT_CLIENT_ID=your_reddit_app_id
REDDIT_CLIENT_SECRET=your_reddit_app_secret
USER_AGENT=reddit-persona-script/0.1 by your_reddit_username
💡 You can get these keys from:

OpenAI: https://platform.openai.com/account/api-keys

Reddit API: https://www.reddit.com/prefs/apps

🔄 Run the Script
bash
Copy
Edit
python main.py <reddit_username_or_url>
Example:

bash
Copy
Edit
python main.py Hungry-Move-6603
📁 Output
Each run creates a .txt file in the same folder, named:

text
Copy
Edit
<username>_persona.txt
Example:

Copy
Edit
kojied_persona.txt
hungry_move_6603_persona.txt
📄 Sample Output Format
text
Copy
Edit
Name: Sarah
Age: 28
Occupation: UX Designer

About:
Sarah is a tech-savvy, open-minded individual who often engages in design and psychology discussions...

Personality Traits:
- Curious
- Empathetic
- Detail-oriented

Hobbies & Interests:
- UI/UX Design
- Indie games

Sample Citations:
- "I'm obsessed with color psychology..." (comment on r/Design)
- "I recently prototyped an app..." (post on r/UXDesign)
📦 Folder Structure
css
Copy
Edit
reddit-persona-generator/
├── main.py
├── .env.example
├── README.md
├── requirements.txt
├── kojied_persona.txt
└── hungry_move_6603_persona.txt
🧑‍💻 Author
Made with ❤️ by Your Name

📜 License
MIT License. Feel free to use and modify.

yaml
Copy
Edit

---

Let me know if you also want:
- Sample `.env.example` file  
- A zipped folder of the whole project  
- GitHub-ready repo template link

I can generate any of these instantly.

