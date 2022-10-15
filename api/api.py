import json
import Utils
from flask import Flask, jsonify, Response

from Utils import get_security_logs

app = Flask(__name__)

@app.route("/get-heatmap")
def route_get_heatmap():
    hm = Utils.get_heatmap_values(Utils.get_security_logs(Utils.DATABASE_FILENAME))
    resp = Response(jsonify(hm))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/get-security-logs")
def route_get_security_logs():
    security_log = get_security_logs(Utils.DATABASE_FILENAME)
    return jsonify(security_log)