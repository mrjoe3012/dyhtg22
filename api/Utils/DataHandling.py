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
    for access in security_logs:
        if(access[2] in building_names_times_dict.keys()): #put here for queen maragret stuff going on
            if not (check_time_in_range(building_names_times_dict[access[2]], access[3])):
                breaches_dict[access[0]] = (access[2], access[3])
    return breaches_dict

  #  dict ret ={}
    # ret = {}
    # for i in security_logs:
    #     out_before = false
    #     if i[0] in ret.keys():
    #         out_before = true

    #     for j in location_data:
    #         if j[0] == i[2]:
    #             warning = time_check(i[3], j[2])
    #             if warning == false and out_before == true:
    #                 temp = (i[2], i[3])
    #                 list_hours = ret[i[0]] 
    #                 list_hours.append(temp)
    #                 ret[i[0]] = list_hours
    #             if warning == false and out_before == false:
    #                 temp = [(i[2], i[3])]
    #                 ret[i[0]] = temp
    #print("hi")
    #print(ret)
    #return ret
    




    
    
    # for i in security_logs:#
 #       temp = i[3].split('-')
  #      if i[0] in ret.keys():
   #         for j in location_data:
    #            temp2 = j[2].split('-')
     #           if j[0] == i[2]:
      #              if (int(temp[0])<int(temp2[0])) or (int(temp[1])>int(temp2[1])):
       #                 temp_list = (j[0],i[3])
        #                dict_list = ret[i[0]]
         #               dict_list.append(temp_list)
          #              ret[i[0]] = dict_list 
        #else:
         #   for y in location_data:
          #      temp2 = y[2].split('-')
           #     if y[0] == i[2]:
            #        if (int(temp[0])<int(temp2[0])) or (int(temp[1])>int(temp2[1])):
             #           temp_list = (y[0], i[3])
              #          ret[i[0]] = [temp_list]
    
    
    
    #print(ret)
    #return ret



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

def display_graph_from_adjacency_matrix(adjacency_matrix):
    graph = nx.from_numpy_matrix(adjacency_matrix)
    # nodes = max(nx.connected_components(graph), key=len)
    # H = nx.subgraph(graph, nodes)
    nx.draw(nx.connected_components(graph))
    plt.show()

def filter_interaction_graph(adjacency_matrix, threshold):
    filtered_adjacency_matrix = np.copy(adjacency_matrix)
    filtered_adjacency_matrix[np.where(adjacency_matrix < threshold)] = 0
    return filtered_adjacency_matrix
