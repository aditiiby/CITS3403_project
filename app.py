from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey123'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=60)])
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/Hydrogen')
def Hydrogen ():
    return render_template('Hydrogen.html')

@app.route('/carbon')
def carbon():
    return render_template('carbon.html')

@app.route('/helium')
def helium():
    return render_template('helium.html')

@app.route('/iron')
def iron():
    return render_template('iron.html')

@app.route('/nitrogen')
def nitrogen():
    return render_template('nitrogen.html')

@app.route('/oxygen')
def oxygen():
    return render_template('oxygen.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data +'</h1>'

    return render_template('login.html', form = form)

if __name__ == '__main__':

    app.run(debug = True) 