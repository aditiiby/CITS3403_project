from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':

    app.run(debug = True) 