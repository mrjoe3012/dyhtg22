from more_itertools import adjacent
import numpy as np
import Utils, unittest

class TestDataHandling(unittest.TestCase):
    
    def test_get_security_breaches(self):
        security_breaches = Utils.detect_security_breaches(Utils.get_security_logs(Utils.DATABASE_FILENAME))
        self.assertTrue("Abdul Murphy" in security_breaches and ("Boyd Orr Building", "2208-2219") in security_breaches["Abdul Murphy"])

    def test_check_time_in_range(self):
        self.assertFalse(Utils.check_time_in_range("0900-1700", "2000-2015")) # out of hours
        self.assertTrue(Utils.check_time_in_range("0900-1700", "0900-1200")) # right on time
        self.assertFalse(Utils.check_time_in_range("0900-1700", "1845-1000")) # out of hours, slept in
        self.assertTrue(Utils.check_time_in_range("0900-1700", "0945-1030")) # in hours
        self.assertTrue(Utils.check_time_in_range("2100-0200", "0120-0200")) # kicked out
        self.assertFalse(Utils.check_time_in_range("2100-0200", "2045-2120")) # out of hours
        self.assertTrue(Utils.check_time_in_range("0000-0000", "1220-1330")) # control - no hours
        self.assertTrue(Utils.check_time_in_range("0000-0000", "0345-0445")) # control - no hours

    def test_check_time_overlap(self):
        self.assertTrue(Utils.check_time_overlap("0900-1200", "0900-1200")) # t
        self.assertFalse(Utils.check_time_overlap("0900-1200", "1201-1220")) # f
        self.assertTrue(Utils.check_time_overlap("2300-0200", "0145-0300")) # t
        self.assertFalse(Utils.check_time_overlap("2345-0100", "2250-2330")) # f
        self.assertTrue(Utils.check_time_overlap("1700-2200", "1730-2300")) # t
        self.assertFalse(Utils.check_time_overlap("0200-0300", "1500-1650")) # f

#if __name__ == "__main__":
#    unittest.main()

#print(Utils.get_security_logs("data/Data"))
#print(Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[0][0:4,:])
#print(Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[1][0:3])
#print(Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[1][58])
#Utils.display_graph_from_adjacency_matrix(Utils.filter_interaction_graph(Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[0], 0))

#print(Utils.detect_security_breaches(Utils.get_security_logs("data/Data")))

#print(Utils.get_adjacency_matrix_for_suspects(Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[0], Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))[1]))
adjacency_mat, student_id_list = Utils.get_meeting_adjacency_matrix(Utils.get_security_logs("data/Data"))
suspects = Utils.get_mastermind(adjacency_mat, student_id_list)[1]
#print(np.where(adjacency_mat[student_id_list.index("2832313W")] > 0))
#print([student_id_list[x] for x in np.where(adjacency_mat[student_id_list.index("2832313W")] > 0)[0] if x in suspects])
#suspects met by Scott Woods
print([student_id_list[x] for x in np.where(adjacency_mat[student_id_list.index("2792337W")] > 0)[0] if x in suspects])
print(Utils.get_mastermind(adjacency_mat, student_id_list)[0])

#person who has interacted with all these paople
#highest amount of interactions
#for each student calculate the total number of itneractions wiith people from this list and the amount
# of people from this list interacted with