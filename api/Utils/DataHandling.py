import sqlite3

def get_security_logs(db_filename):
    query = "SELECT * FROM Security_Logs"
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
    for tuple in get_security_logs("data/Data"):
        if(tuple[2] in occurrence_dict.keys()):
            occurrence_dict[tuple[2]] += 1

    return occurrence_dict