from flask import Flask, render_template, request, redirect
from database.operations import insert
from api import get_json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front-page.html')

@app.route('/api/all')
def api():
    return get_json()

if __name__ == "__main__":
    app.run(port=5000)