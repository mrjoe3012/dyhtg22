from array import array
from io import BytesIO
import sqlite3

from sympy import false, true
import pandas as pd
import string
import Utils
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_security_logs(db_filename):
    query = "SELECT * FROM Security_Logs"
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    cur.execute(query)
    query_result = cur.fetchall()
    return query_result

def get_buildings(db_filename):
    query = "SELECT * FROM location_data"
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    cur.execute(query)
    query_result = cur.fetchall()
    return query_result

def get_people_data(db_filename):
    query = "SELECT * FROM People_Data"
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    cur.execute(query)
    query_result = cur.fetchall()
    data = []
    for row in query_result:
        entry = {}
        entry["id"] = row[0]
        entry["name"] = row[1]
        entry["age"] = int(row[2])
        entry["sex"] = row[3]
        entry["year"] = row[4]
        entry["subject"] = row[5]
        entry["height"] = int(row[6])
        entry["hair"] = row[7]
        socs = row[8].strip()
        socs = socs.replace("[","").replace("]","").replace("'","")
        entry["societies"] = socs
        data.append(entry)
    return data
        

def get_heatmap_values(security_logs):
    # python array of tuples, all containing strings with 
    occurrence_dict = {"Boyd Orr Building": 0,
                        "James Watt Building": 0,
                        "Adam Smith Building": 0,
                        "Main Building": 0,
                        "Wolfson Medical Building": 0,
                        "Glasgow University Union": 0,
                        "The Hive": 0,
                        "Sir Alwyn Williams Building": 0,
                        "Library": 0,
                        "Queen Margaret Union": 0,
                        "St Andrews Building": 0,
                        "Kelvingrove Park": 0,
                        "Joseph Black Building": 0,
                        "Kelvin Building" :0
                        }
    for tuple in get_security_logs(Utils.DATABASE_FILENAME):
        if(tuple[2] in occurrence_dict.keys()):
            occurrence_dict[tuple[2]] += 1

    return occurrence_dict

# returns the time difference in minutes between
# time2 and time 1
def time_difference(time1, time2):
    if time2 < time1:
        time2 += 2400
    return time2 - time1

# returns true if the two time ranges overlap
# e.g. 
# check_time_overlap("2100-2200", "2150-2220") = True
# check_time_overlap("2350-0100", "0010-0200") = True
# check_time_overlap("1600-1800", "1900-2100") = False
def check_time_overlap(time_range_1, time_range_2):
    time1_ints, time2_ints = [int(x) for x in time_range_1.split("-")], [int(x) for x in time_range_2.split("-")]
    time1_difference = time_difference(time1_ints[0], time1_ints[1])
    time2_difference = time_difference(time2_ints[0], time2_ints[1])
    return (time_difference(time1_ints[0], time2_ints[0]) <= time1_difference or time_difference(time1_ints[0], time2_ints[1]) <= time1_difference) or (time_difference(time2_ints[0], time1_ints[0]) <= time2_difference or time_difference(time2_ints[0], time1_ints[1]) <= time2_difference)

# returns true if check_time is within the time_range
# e.g.
# check_time_in_range("0900-1700", "1000-1200") = True
# check_time_in_range("2200-0200", "0100-0300") =
def check_time_in_range(time_range, check_time):
    if time_range == "0000-0000": return True
    time1_ints, time2_ints = [int(x) for x in time_range.split("-")], [int(x) for x in check_time.split("-")]
    time1_difference = time_difference(time1_ints[0], time1_ints[1])
    return (time_difference(time1_ints[0], time2_ints[0]) <= time1_difference and time_difference(time1_ints[0], time2_ints[1]) <= time1_difference)

def detect_security_breaches(security_logs):
    # go through security logs
    # find out when a building is visited out of hours
    # return a mapping from student ids to breach=(building,hours_visited)
    breaches_dict = {}
    location_data = get_buildings(Utils.DATABASE_FILENAME)
    stripped_location_data = np.delete(np.delete(np.array(location_data)[1:],obj=1,axis=1),obj=2,axis=1) #only building name and opening times
    building_names_times_dict = {}
    for line in stripped_location_data:
        building_names_times_dict[line[0]] = line[1]
    del building_names_times_dict["Kelvingrove Park"] #delete kelvingrove as it does not have opening times

def get_meeting_adjacency_matrix(security_logs):
    #each element in security_logs is a building interaction
    #each student can interact many times
    student_ids = []
    for tuple in security_logs:
        if tuple[0] not in student_ids:
            student_ids.append(tuple[0]) #storing ids in order of occurrence in the logs without duplicates
    adjacency_matrix = np.zeros((len(student_ids), len(student_ids)))
    #np.fill_diagonal(adjacency_matrix,0)
    #make another dictionary mapping student ids to indices
    #while loop until you find an entry time that's after that particular student's exit time
    for i in range(len(security_logs)):
        j = i + 1
        count = 0
        while count != len(security_logs):
            if(j == len(security_logs)):
                j = 0
            if not (check_time_overlap(security_logs[i][3], security_logs[j][3])):
                break
            elif (security_logs[i][0] != security_logs[j][0]) and (security_logs[i][2] == security_logs[j][2]):
                adjacency_matrix[student_ids.index(security_logs[i][0])][student_ids.index(security_logs[j][0])] += 1
                adjacency_matrix[student_ids.index(security_logs[j][0])][student_ids.index(security_logs[i][0])] += 1
            j += 1
            count += 1
    return adjacency_matrix, student_ids

def get_dict_from_adjacency_matrix(adjacency_matrix, student_ids):
    interaction_dict = {}
    for student_id in student_ids:
        adjacency_matrix_current_row = adjacency_matrix[student_ids.where(student_id)]
        for i in range(adjacency_matrix_current_row.len()):
            if (adjacency_matrix_current_row[i] > 0):
                interaction_dict[student_id].append((student_ids[i], adjacency_matrix_current_row[i]))
    return interaction_dict

def display_graph_from_adjacency_matrix(adjacency_matrix, student_ids, show=True):
    graph = nx.from_numpy_matrix(adjacency_matrix)
    # nodes = max(nx.connected_components(graph), key=len)
    # H = nx.subgraph(graph, nodes)
    mapping = {x : student_ids[x] for x in range(len(student_ids))}
    graph = nx.relabel_nodes(graph, mapping)
    graph.remove_nodes_from(list(nx.isolates(graph)))
    plt.close()
    nx.draw(graph, with_labels=True)
    if show:
        plt.show()
    else:
        bytes = BytesIO()
        plt.savefig(bytes, format="png")
        bytes.seek(0)
        # get data with bytes.read()
        return bytes

def filter_interaction_graph(adjacency_matrix, threshold):
    filtered_adjacency_matrix = np.copy(adjacency_matrix)
    #filtered_adjacency_matrix[np.where(adjacency_matrix < threshold)] = 0
    filtered_adjacency_matrix[filtered_adjacency_matrix < threshold] = 0
    return filtered_adjacency_matrix

def get_adjacency_matrix_for_suspects(adjacency_matrix, student_ids):
    relevant_id_indices = np.array([student_ids.index("2774868P"), 
                            student_ids.index("2546112P"),
                            student_ids.index("2912324G"),
                            student_ids.index("2786843M"),
                            student_ids.index("2456431B"),
                            student_ids.index("2446198D"),
                            student_ids.index("2558094B"),
                            student_ids.index("2453876J")])
    print(relevant_id_indices)
    print(adjacency_matrix.shape)
    suspect_adj_matrix = np.take(adjacency_matrix, relevant_id_indices, axis=0)
    suspect_adj_matrix = np.take(suspect_adj_matrix, relevant_id_indices, axis=1)
    return suspect_adj_matrix

def get_adjacency_matrix_for_given_student_ids(adjacency_matrix, student_ids, student_ids_to_include, strict=False):
    if not strict:
        student_id_minus = list(student_ids)
        indices_for_student_ids_to_include = []
        for id in student_ids_to_include:
            student_id_minus.remove(id)
        for i, student_id_to_include in enumerate(student_id_minus):
            indices_for_student_ids_to_include.append(student_ids.index(student_id_to_include))
        indices_for_student_ids_to_include = np.array(indices_for_student_ids_to_include)
        #print(relevant_id_indices)
        #print(adjacency_matrix.shape)
        #print(indices_for_student_ids_to_include.dtype)
        #np.fill_diagonal(adjacency_matrix, 1)
        #specific_adj_matrix = np.take(adjacency_matrix, np.where(adjacency_matrix[indices_for_student_ids_to_include] > 0), axis=0)
        specific_adj_matrix = np.copy(adjacency_matrix)
        specific_adj_matrix[indices_for_student_ids_to_include,:] = 0
        #specific_adj_matrix = np.take(specific_adj_matrix, np.where(specific_adj_matrix[indices_for_student_ids_to_include] > 0), axis=1)
        return specific_adj_matrix
    else:
        indices_for_student_ids_to_include = np.zeros(len(student_ids_to_include), dtype=np.int64)
        for i,id in enumerate(student_ids_to_include):
            indices_for_student_ids_to_include[i] = student_ids.index(id)
        specific_adj_matrix = np.take(adjacency_matrix, indices_for_student_ids_to_include, axis=0)
        specific_adj_matrix = np.take(specific_adj_matrix, indices_for_student_ids_to_include, axis=1)
        return specific_adj_matrix

def get_mastermind(adjacency_matrix, student_ids):
    interaction_with_suspects_list = []
    number_of_connection_list = []
    relevant_id_indices = np.array([student_ids.index("2774868P"), 
                            student_ids.index("2546112P"),
                            student_ids.index("2912324G"),
                            student_ids.index("2786843M"),
                            student_ids.index("2456431B"),
                            student_ids.index("2446198D"),
                            student_ids.index("2558094B"),
                            student_ids.index("2453876J")])
    for i, student_id in enumerate(student_ids):
        interaction_with_suspects_list.append((student_id, len(np.where(adjacency_matrix[i][relevant_id_indices]>0)[0])))
        interaction_with_suspects_list = sorted(interaction_with_suspects_list, key=lambda x:x[1])[::-1]
    for i,row in enumerate(adjacency_matrix):
        number_of_connection_list.append((student_ids[i], len(np.where(row > 0)[0])))
    number_of_connection_list = sorted(number_of_connection_list, key=lambda x:x[1])[::-1]
    return interaction_with_suspects_list, relevant_id_indices