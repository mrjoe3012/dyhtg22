import sqlite3

from sympy import false, true
import Utils
import pandas as pd

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


def time_check(time_open, time_log):
    splitted_log = time_log.split("-")
    split_open = time_open.split("-")
    int_log =[]
    int_open =[]
    for i in range(2):
        int_log.append(int(splitted_log[i]))
        int_open.append(int(split_open[i]))
    out_hours = false
    print(str(int_log[0]) + "temp")
    entry = false
    exit = false
    print(int_log[0]<= int_open[1])
    print(int_log[1], int_open[1])
    if (int_log[0] <= int_open[1] and int_log[0] >= int_open[0]) or (int_log[0] <= int_open[1] or int_log[0] >= int_open[0]) :
        entry = true

    if int_log[1] >= int_open[0] and int_log[1] <= int_open[1]:
        exit = true
    print(entry, exit)
    if entry == true and exit == true:
        return true
    else: return false
    
    
    

    return false

## if 2230 hours 0100
# 2230 and 9
def detect_security_breaches(security_logs):
    location_data = get_buildings(Utils.DATABASE_FILENAME)
    print(location_data)
    print(security_logs)

    #building data ('Building Name', 'Geolocation', 'Opening Times', 'Description')
    #security logs ("Student ID", "name", "location", "time")


  #  dict ret ={}
    ret = {}
    for i in security_logs:
        out_before = false
        if i[0] in ret.keys():
            out_before = true

        for j in location_data:
            if j[0] == i[2]:
                warning = time_check(i[3], j[2])
                if warning == false and out_before == true:
                    temp = (i[2], i[3])
                    list_hours = ret[i[0]] 
                    list_hours.append(temp)
                    ret[i[0]] = list_hours
                if warning == false and out_before == false:
                    temp = [(i[2], i[3])]
                    ret[i[0]] = temp
    print("hi")
    print(ret)
    return ret
    




    
    
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
    return ret



    # go through security logs
    # find out when a building is visited out of hours
    # return a mapping from student ids to breach=(building,hours_visited)
        # pass