from flask import Flask, render_template
#from flask_bootstrap import Bootsrap

#bootstrap = Bootstrap(app)

app = Flask(__name__)

@app.route('/page')
def hello():
    return '<h1> hello there this works! </h1>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pic')
def funny():
    return render_template('picture.html')


app.run()