
from flask import Flask, render_template, request, jsonify
from data import portfolio_data
import os
from dotenv import load_dotenv
from groq import Groq
import pypdf

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

# Extract Resume Text
resume_text = ""
try:
    reader = pypdf.PdfReader('2026_Resume.pdf')
    for page in reader.pages:
        resume_text += page.extract_text() + "\n"
except Exception as e:
    print(f"Error reading resume: {e}")
    # Fallback to data.py content if PDF fails
    import json
    resume_text = json.dumps(portfolio_data, indent=2)

SYSTEM_PROMPT = f"""
You are a helpful AI assistant for Ronak Pradhan's portfolio website.
Your goal is to answer questions about Ronak based ONLY on the following resume content:

{resume_text}

If the answer is not in the resume, politely say you don't have that information.
Keep answers concise, professional, and friendly.
"""

@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=portfolio_data, active='dashboard')

@app.route('/experience')
def experience():
    return render_template('experience.html', data=portfolio_data, active='experience')

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data, active='projects')

@app.route('/skills')
def skills():
    return render_template('skills.html', data=portfolio_data, active='skills')
    
@app.route('/education')
def education():
    return render_template('education.html', data=portfolio_data, active='education')

@app.route('/chat', methods=['POST'])
def chat():
    if not client:
        return jsonify({"error": "Chatbot not configured (Missing API Key)"}), 500
    
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        response = chat_completion.choices[0].message.content
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
