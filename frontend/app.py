from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static/js')
@app.route('/')
def hello_world():
    return render_template('index.html')

