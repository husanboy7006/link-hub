import json
import os
from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    try:
        # Use absolute path to ensure file is found in Vercel environment
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_path, 'links.json')
        
        with open(data_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "name": "User Name", 
            "bio": "Bio goes here", 
            "avatar": "", 
            "links": []
        }

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/portfolio')
def portfolio():
    data = load_data()  # To keep profile info available
    projects = [
        {
            "title": "Elektronika CRM",
            "description": "Elektronika do'konlari uchun savdo va ombor nazorati tizimi.",
            "link": "#",
            "icon": "fas fa-desktop"
        },
        {
            "title": "Marketing Audit",
            "description": "Biznes marketing holati va byudjetini analiz qiluvchi maxsus dashboard.",
            "link": "#",
            "icon": "fas fa-chart-line"
        },
        {
            "title": "Telegram Bot",
            "description": "Instagram va YouTube'dan video yuklab beruvchi bot.",
            "link": "#",
            "icon": "fab fa-telegram-plane"
        }
    ]
    return render_template('portfolio.html', data=data, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
