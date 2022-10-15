import json
import Utils
from flask import Flask, jsonify

from Utils import get_security_logs

app = Flask(__name__)

@app.route("/get-security-logs")
def route_get_security_logs():
    security_log = get_security_logs(Utils.DATABASE_FILENAME)
    return jsonify(security_log)