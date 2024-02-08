"## ChatGPT"
import os
import openai
from openai import OpenAI
import sys
from flask import Flask, render_template, request, jsonify
from openai_token import openai_api_key

class ChatApp:
    def __init__(self, openai_api_key):
        # Setting the API key to use the OpenAI API
        openai.api_key = openai_api_key
        self.messages = []

    def chat(self, message, model="gpt-4"):
        self.messages.append({"role": "user", "content": message})
        response = client.chat.completions.create(
            model = model,
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content

    def new_chat(self):
        self.messages = []
        print(f"Chat reset, messages {self.messages}")


client = OpenAI(api_key=openai_api_key)
chat = ChatApp(openai_api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.json['text']
    result = process_input(chat, text)
    # Process the text as needed, here we just return it reversed as an example
    return jsonify({"reply": result})


def test():
    chat = ChatApp(openai_api_key)
    print(chat.chat('Tell me a joke'))
    print(chat.chat("What's funny in this joke?"))

def process_input(chat, text):
    # Example processing: reverse the input text
    return chat.chat(text)

if __name__ == "__main__":

    app.run()

