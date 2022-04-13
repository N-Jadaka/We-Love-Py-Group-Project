from email import message
from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)
env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)
@app.route('/')
def root():
    message = "This is our homepage"
    return render_template("index.html", msg=message)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/connie-page')
def login():
    data = ""
    return render_template("conn.html")

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/test')
# @app.route('/test/<name>')
def test():
    return render_template('./index.html')