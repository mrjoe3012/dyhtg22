import sqlite3
import string
import Utils

def verify_time_format(time_string):
    if type(time_string) != string or len(time_string) == 0:
        return False
    time_split = time_string.split("-")
    if len(time_split) != 2:
        return False
    time_ints = [int(x) for x in time_split]
    for x in time_ints:
        if x < 0 or x > 2359:
            return False
    if time_ints[1] < time_ints[0]:
        return False
    return True

def get_security_logs(db_filename):
    query = "SELECT * FROM Security_Logs"
    con = sqlite3.connect(db_filename)
    cur = con.cursor()
    cur.execute(query)
    query_result = cur.fetchall()
    result = []
    for row in query_result:
        time = row[4]
        if verify_time_format(time):
            result.append(row)
    return result

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