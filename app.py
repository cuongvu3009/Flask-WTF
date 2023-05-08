from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
   username = StringField('username', validators=[InputRequired(), Length(min=2, max=20)])
   password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)])

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'MySecretKey!'
    
    @app.route('/', methods=['GET', 'POST'])
    def index(): 
      form = LoginForm()

      if form.validate_on_submit(): 
         return f'<h1>Username: {form.username.data} Password: {form.password.data}</h1>'
      
      return render_template('index.html', form=form)

    return app