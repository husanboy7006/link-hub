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
            "title": "Lead Generation Page",
            "description": "Mijozlarni yig'ishga mo'ljallangan, yuqori konversiyali professional landing page.",
            "link": "https://lendingpeaj-crm.vercel.app",
            "github_link": "https://github.com/husanboy7006/lendingpeaj-crm",
            "category": "web",
            "icon": "fas fa-magnet"
        },
        {
            "title": "CVV APP (Redesign)",
            "description": "GatsbyJS uslubidagi zamonaviy va minimalist interfeysga ega dashboard.",
            "link": "https://marketing-hisobot.vercel.app",
            "github_link": "https://github.com/husanboy7006/marketing-hisobot",
            "category": "crm",
            "icon": "fas fa-vector-square"
        },
        {
            "title": "Reja App",
            "description": "Biznes rejalari va maqsadlarini boshqarish uchun strategik dastur.",
            "link": "https://rejaflow.onrender.com",
            "github_link": "https://github.com/husanboy7006/rejaflow",
            "category": "crm",
            "icon": "fas fa-bullseye"
        },
        {
            "title": "Telegram Mini App",
            "description": "Telegram bot ichida ishlovchi interaktiv veb-interfeys va katalog.",
            "link": "https://telegram-shop-epas.onrender.com",
            "github_link": "https://github.com/husanboy7006/telegram-shop",
            "category": "bot",
            "icon": "fab fa-telegram"
        }
    ]
    return render_template('portfolio.html', data=data, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
