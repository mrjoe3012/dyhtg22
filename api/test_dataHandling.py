import Utils, unittest

class TestDataHandling(unittest.TestCase):
    
    def test_get_security_breaches(self):
        security_breaches = Utils.detect_security_breaches(Utils.get_security_logs(Utils.DATABASE_FILENAME))
        self.assertTrue("Abdul Murphy" in security_breaches and ("Boyd Orr Building", "2208-2219") in security_breaches["Abdul Murphy"])

if __name__ == "__main__":
    unittest.main()