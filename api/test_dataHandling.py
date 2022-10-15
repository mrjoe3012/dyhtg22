import Utils, unittest

class TestDataHandling(unittest.TestCase):
    
    def test_get_security_breaches(self):
        security_breaches = Utils.detect_security_breaches(Utils.get_security_logs(Utils.DATABASE_FILENAME))
        self.assertTrue("Abdul Murphy" in security_breaches and ("Boyd Orr Building", "2208-2219") in security_breaches["Abdul Murphy"])

    def test_time_check(self):
        self.assertTrue(Utils.time_check("0900-1700", "2000-2015")) # out of hours
        self.assertTrue(Utils.time_check("0900-1700", "0900-1200")) # right on time
        self.assertTrue(Utils.time_check("0900-1700", "1845-1000")) # out of hours, slept in
        self.assertTrue(Utils.time_check("0900-1700", "0945-1030")) # in hours
        self.assertTrue(Utils.time_check("2100-0200", "0120-0200")) # kicked out
        self.assertTrue(Utils.time_check("2100-0200", "2045-2120")) # out of hours
        self.assertTrue(Utils.time_check("0000-0000", "1220-1330")) # control - no hours
        self.assertTrue(Utils.time_check("0000-0000", "0345-0445")) # control - no hours

if __name__ == "__main__":
    unittest.main()