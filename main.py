from flask import Flask, request,render_template, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
app = Flask(__name__,template_folder="templates")
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
@app.route('/')
def home():
    return render_template('chatbot.html')
@app.route('/messager',methods=['POST'])
def messager():
    user_msg = request.get_json()['message']
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Agriculture assistant."},
            {"role": "user", "content": user_msg}
        ]
    )
    bot_response=completion.choices[0].message.content.strip()
    return bot_response
if __name__ == '__main__':
    app.run(debug=True)
