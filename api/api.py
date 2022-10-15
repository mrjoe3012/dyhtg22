import json
import Utils
from flask import Flask, jsonify, Response

from Utils import get_security_logs

app = Flask(__name__)

def set_response_headers(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"

@app.route("/get-heatmap")
def route_get_heatmap():
    hm = Utils.get_heatmap_values(Utils.get_security_logs(Utils.DATABASE_FILENAME))
    resp = jsonify(hm)
    set_response_headers(resp)
    return resp

@app.route("/get-security-logs")
def route_get_security_logs():
    security_log = get_security_logs(Utils.DATABASE_FILENAME)
    return jsonify(security_log)

@app.route("/get-people")
def route_get_people():
    people = Utils.get_people_data(Utils.DATABASE_FILENAME)
    print(people)
    resp = jsonify(people)
    set_response_headers(resp)
    return resp
