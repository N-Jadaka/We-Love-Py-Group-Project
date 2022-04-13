from email import message
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def root():
    members = [ 'Connie', 'Lap', 'Josh', 'Katherine']
    return render_template("index.html", team=members)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/connie-page')
def login():
    return render_template("conn.html")

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/test')
# @app.route('/test/<name>')
def test():
    return render_template('./index.html')