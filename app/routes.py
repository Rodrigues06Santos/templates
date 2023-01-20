from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')