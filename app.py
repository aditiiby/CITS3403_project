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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')

if __name__ == '__main__':

    app.run(debug = True) 