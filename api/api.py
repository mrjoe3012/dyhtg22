import time
from flask import Flask

app = Flask(__name__)

@app.route("/get-heatmap-data")
def route_get_heatmap_data():
    # gianmarco
    # get security logs
    # get heatmap values
    # return json of heatmap values
    return "<h1>Hello, not implemented</h1>"