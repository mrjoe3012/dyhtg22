import json
from numpy import full

import Utils
from flask import Flask, jsonify, Response, request, make_response

from Utils import get_security_logs, get_meeting_adjacency_matrix, get_adjacency_matrix_for_given_student_ids, display_graph_from_adjacency_matrix

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
def route_get_interaction_graph():
    args = request.args #students=(id,id,id,...) args[0]=(id,id,...)
    args_dict = args.to_dict() #args_dict.get("students")
    #student_filter_list = args_dict["students"].split(",")
    student_ids_to_display = args_dict.get("students").split(",")
    print(student_ids_to_display)
    full_adjacency_matrix, student_ids = get_meeting_adjacency_matrix(get_security_logs(Utils.DATABASE_FILENAME))
    if len(student_ids_to_display) > 0 and student_ids_to_display[0] != "":
        for student_id in student_ids_to_display:
            if student_id not in student_ids:
                student_ids_to_display.pop(student_ids_to_display.index(student_id))
        adjacency_matrix_to_display = get_adjacency_matrix_for_given_student_ids(full_adjacency_matrix, student_ids, student_ids_to_display)
    else:
        adjacency_matrix_to_display = full_adjacency_matrix
    byte_representation = display_graph_from_adjacency_matrix(adjacency_matrix_to_display, student_ids, show=False)



    response = make_response(byte_representation.read())
    response.headers["Content-Type"] = "image/png"
    set_response_headers(response)
    return response

    #handle request arguments (parse a comma separated list) if list is empty it means no filter, return all student_ids, if there is any ids that are not real, return nothing
    #get adjacency matrix
    #filter based on student ids
    #get binary representation with joe's display_adj_matrix method
    #create response format with mine type image/png
    #return response
