import unittest
from test_chromium import run as chromium_run
from test_firefox import run as firefox_run

class Test_All(unittest.TestCase):

    def testChromium(self):
        self.assertTrue(chromium_run())

    def testFirefox(self):
        self.assertTrue(firefox_run())

if __name__ == "__main__":
    unittest.main()