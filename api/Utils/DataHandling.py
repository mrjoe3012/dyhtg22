import sqlite3
import Utils

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
    for tuple in get_security_logs(Utils.DATABASE_FILENAME):
        if(tuple[2] in occurrence_dict.keys()):
            occurrence_dict[tuple[2]] += 1

    return occurrence_dict

# returns a time range where the exit is always greater than entry:
# e.g.
# 0900-1200 -> 0900-1200 (no change)
# 2200-0200 -> 2200-2600 (0200 -> 2400 + 0200)
def make_time_friendly(time_range):
    times = [int(x) for x in time_range.split("-")]
    if times[1] > times[0]:
        return time_range
    else:
        times[1] += 2400
        new_time_range = "{0}-{1}".format(times[0],times[1])
        return new_time_range

# returns true if the two time ranges overlap
# e.g. 
# check_time_overlap("2100-2200", "2150-2220") = True
# check_time_overlap("2350-0100", "0010-0200") = True
# check_time_overlap("1600-1800", "1900-2100") = False
def check_time_overlap(time_range_1, time_range_2):
    # revert mod 2400 behaviour of time
    time_range_1_friendly, time_range_2_friendly = make_time_friendly(time_range_1), make_time_friendly(time_range_2)
    times_1, times_2 = [int(x) for x in time_range_1.split("-")], [int(x) for x in time_range_2.split("-")]
    
    # return time_range_1 ∩ time_range_2 ≠ Ø
    return (times_1[0] >= times_2[0] and times_1[0] <= times_2[1]) or (times_2[0] >= times_1[0] and times_2[0] <= times_2[1])

# returns true if check_time is within the time_range
# e.g.
# check_time_in_range("0900-1700", "1000-1200") = True
# check_time_in_range("2200-0200", "0100-0300") =
def check_time_in_range(time_range, check_time):
    # revert mod 2400 behaviour of time
    time_range_friendly, check_time_friendly = make_time_friendly(time_range), make_time_friendly(check_time)
    times_range_ints, check_time_ints = [int(x) for x in time_range_friendly.split("-")], [int(x) for x in check_time_friendly.split("-")]

    # return check_time ⊆ time_range
    return (check_time_ints[0] >= time_range_ints[0] and check_time_ints[0] <= time_range_ints[1]) and (check_time_ints[1] >= time_range_ints[0] and check_times_ints[1] <= time_range_ints[1])

def detect_security_breaches(security_logs):
    # go through security logs
    # find out when a building is visited out of hours
    # return a mapping from student ids to breach=(building,hours_visited)
    pass
