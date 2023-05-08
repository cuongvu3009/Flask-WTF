from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, EmailField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
   username = StringField('Your username', validators=[InputRequired(), Length(min=2, max=20)])
   password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)])
   age = IntegerField('age', validators=[InputRequired()])
   email = EmailField('email', validators=[InputRequired()])
   subscribe = BooleanField('Subscribe to news letter', default=True)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey!'
    
    @app.route('/', methods=['GET', 'POST'])
    def index(): 
      form = LoginForm()

      if form.validate_on_submit(): 
         return f'<h1>Username: {form.username.data} | Password: {form.password.data} | Age: {form.age.data} | Email: {form.email.data} | Subscribe: {form.subscribe.data}</h1>'
      
      return render_template('index.html', form=form)

    return app