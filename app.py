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

if __name__ == '__main__':
    app.run(debug=True)
