import json
from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    try:
        with open('links.json', 'r') as f:
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

if __name__ == '__main__':
    app.run(debug=True)
