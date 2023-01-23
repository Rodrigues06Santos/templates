from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import SendForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = SendForm()
    if form.validate_on_submit():
        mensagem = flash('A mensagem foi enviada com sucesso')
    return render_template('contato.html', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')