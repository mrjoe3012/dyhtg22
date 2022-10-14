import time
from flask import Flask

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    return {"time" : time.time()}

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>\n<p>(this means that flask is working!)</p>"
