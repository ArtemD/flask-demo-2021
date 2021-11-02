from flask import Flask, render_template, request, redirect
from database.operations import insert
from api import get_json

app = Flask(__name__)

@app.route('/form')
def form():
    """ Display submission form """
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='GET':
        return redirect('/form')
    else:
        if insert(request.form['name'], request.form['address'], request.form['postcode'], 
                request.form['city'],request.form['date'], request.form['type'], 
                request.form['businessid']):
            return "Data inserted"
        else:
            return "Data not inserted"

@app.route('/')
def index():
    return render_template('front-page.html')

@app.route('/api/all')
def api():
    return get_json()

if __name__ == "__main__":
    app.run(port=5000)