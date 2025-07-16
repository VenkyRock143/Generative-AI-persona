import os
import re
import sys
import openai
import praw
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT", "reddit-persona-script")
)

def extract_username(url_or_name: str) -> str:
    """Extracts Reddit username from full URL or returns the name directly"""
    match = re.search(r'reddit\.com/user/([a-zA-Z0-9_-]+)', url_or_name)
    return match.group(1) if match else url_or_name

def fetch_user_content(username):
    """Fetches recent posts and comments of the user"""
    user = reddit.redditor(username)
    posts, comments = [], []

    try:
        for post in user.submissions.new(limit=20):
            posts.append((post.title, post.selftext))
        for comment in user.comments.new(limit=50):
            comments.append(comment.body)
    except Exception as e:
        print(f"❌ Error fetching user data: {e}")
    return posts, comments

def generate_persona(username, posts, comments):
    """Generates a structured user persona with citations"""
    content = "\n\n".join(
        [f"Post Title: {title}\n{body}" for title, body in posts] +
        [f"Comment: {c}" for c in comments]
    )

    prompt = f"""
You are an expert user researcher. Build a detailed **User Persona** based on this Reddit user's public activity.

Use this structured format:

Name: (Give a fictional first name)
Age: (Estimate if possible)
Occupation: (Guess based on content)
Location: (Only if implied)

About:
(Short paragraph summarizing the user’s background and lifestyle)

Personality Traits:
- Trait 1
- Trait 2
- Trait 3

Hobbies & Interests:
- Interest 1
- Interest 2

Goals:
- Goal 1
- Goal 2

Challenges or Pain Points:
- Challenge 1
- Challenge 2

Online Behavior:
- Writing tone (e.g., humorous, serious)
- Most active subreddits or topics
- How they express themselves

Sample Citations:
After each insight, include relevant snippets from Reddit content that support the point.
Use quotes like:
- "I’ve been struggling with anxiety..." (comment on r/anxiety)
- "I love building side projects..." (post on r/learnprogramming)

Reddit Content:
{content}
    """

    print("🔁 Generating persona using GPT...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ GPT Error: {e}")
        return "Error generating persona."

def save_persona(username, text):
    filename = f"{username.lower()}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Persona saved as {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url_or_username>")
        sys.exit(1)

    input_arg = sys.argv[1]
    username = extract_username(input_arg)
    print(f"🔍 Extracted username: {username}")

    posts, comments = fetch_user_content(username)
    if not posts and not comments:
        print("❌ No Reddit data found.")
        sys.exit(1)

    persona_text = generate_persona(username, posts, comments)
    save_persona(username, persona_text)
