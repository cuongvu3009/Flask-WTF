from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
   username = StringField('username')
   password = PasswordField('password')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey!'
    
    @app.route('/', methods=['GET', 'POST'])
    def index(): 
      form = LoginForm()
      return render_template('index.html', form=form)

    return app