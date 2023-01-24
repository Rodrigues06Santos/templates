from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import SendForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo = 'home')

@app.route('/contato', methods = ['POST', 'GET'])
def contato():
    form = SendForm()
    if form.validate_on_submit():
        mensagem = flash('A mensagem foi enviada com sucesso')
    return render_template('contato.html', form=form, titulo = 'contato')

@app.route('/blog')
def blog():
    return render_template('blog.html', titulo = 'blog')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'sobre')