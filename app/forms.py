from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
class SendForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    mensagem = StringField('mensagem', validators=[DataRequired()])
    assunto = TextAreaField('assunto', validators=[DataRequired()])
    submit = SubmitField('enviar')