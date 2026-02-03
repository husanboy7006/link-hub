from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_data():
    try:
        with open('links.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "name": "Husan",
            "bio": "Ma'lumotlar topilmadi",
            "profile_image": "",
            "links": []
        }

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
