'''
Need some testing...
'''
import unittest
from roomwifiservice import generate_token

class TestRoomWifiService(unittest.TestCase):
    def test_generate_token(self):
        newtoken = generate_token()
        self.assertIsInstance(newtoken, str)