from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test_output():
    return 'Hello Katherine, Connie, and Lap '

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/about')
def about():
    return 'about'

@app.route('/test')
# @app.route('/test/<name>')
def test():
    return render_template('./index.html')