from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import json




app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(60), unique=True)
    hydrogenResults = db.Column(db.Integer)
    heliumResults = db.Column(db.Integer)
    carbonResults = db.Column(db.Integer)
    nitrogenResults = db.Column(db.Integer)
    oxygenResults = db.Column(db.Integer)
    ironResults = db.Column(db.Integer)

    def getId(self):
        return self.id

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=30)])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=60)])
    username = StringField('username', validators=[InputRequired(), Length(min=8, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=30)])


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/hydrogen',methods=['GET','POST'])
def hydrogen ():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.hydrogenResults = result
            print(result)
            db.session.commit()
    return render_template('Hydrogen.html')
    

@app.route('/carbon',methods=['GET','POST'])
def carbon():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.carbonResults = result
            db.session.commit()
    return render_template('carbon.html')

@app.route('/helium',methods=['GET','POST'])
def helium():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.heliumResults = result
            db.session.commit()
    return render_template('helium.html')

@app.route('/iron',methods=['GET','POST'])
def iron():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.ironResults = result
            db.session.commit()
    return render_template('iron.html')

@app.route('/nitrogen',methods=['GET','POST'])
def nitrogen():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.nitrogenResults = result
            db.session.commit()
    return render_template('nitrogen.html')

@app.route('/oxygen',methods=['GET','POST'])
def oxygen():
    if request.method == 'POST':
        result = request.get_json()
        if result != None:
            current_user.oxygenResults = result
            db.session.commit()
    return render_template('oxygen.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nav')
def nav():
    if current_user.is_authenticated:
        return render_template('navLogout.html', data = current_user.username)
    return render_template('nav.html')

@login_required
@app.route('/profile')
def profile():
    if not current_user.is_authenticated:
        return render_template('index.html')
    return render_template('profile.html', oxygenResults = current_user.oxygenResults, hydrogenResults = current_user.hydrogenResults )




@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                login_user(user)
                return render_template('lessons.html')
        return render_template('login.html', form = form)
    return render_template('login.html', form = form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        newUser = User(username = form.username.data, password = form.password.data, email = form.email .data)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)
        return render_template('profile.html')
    return render_template('signup.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')



if __name__ == '__main__':

    app.run(debug = True) 