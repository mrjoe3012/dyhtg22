import json
import Utils
from flask import Flask, jsonify, Response, make_response, send_file

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
    # print(people)
    resp = jsonify(people)
    set_response_headers(resp)
    return resp

@app.route("/get-interaction-graph")
def xxx():
    adj, students = Utils.get_meeting_adjacency_matrix(Utils.get_security_logs(Utils.DATABASE_FILENAME))
    adj = adj[0:10,0:10]
    bytes = Utils.display_graph_from_adjacency_matrix(adj, students, show=False)
    response = make_response(bytes.read())
    set_response_headers(response)
    response.headers.set('Content-Type', 'image/png')
    return response