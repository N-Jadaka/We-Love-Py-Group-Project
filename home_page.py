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

@app.route('/connie-page', methods=['GET', 'POST'])
def connie():
    return render_template("conn.html")

@app.route('/lap', methods=['GET', 'POST'])
def lap():
    return render_template("lap.html")

@app.route('/josh', methods=['GET', 'POST'])
def josh():
    return render_template("josh.html")

@app.route('/katherine', methods=['GET', 'POST'])
def katherine():
    return render_template("josh.html")
