import os
import unittest
import json
from src.utils import get_gmail_account_from_file, spoof_ip, rand_int


class TestUtils(unittest.TestCase):
    def test_get_gmail_account_from_file(self):
        with open('test.json', 'w') as f:
            data = {"account": "example@gmail.com", "password": "password123"}
            json.dump(data, f)

        account, password = get_gmail_account_from_file('test.json')
        self.assertEqual(account, 'example@gmail.com')
        self.assertEqual(password, 'password123')

        os.remove('test.json')

    def test_spoof_ip(self):
        ip = spoof_ip()
        self.assertTrue(isinstance(ip, str))
        self.assertRegex(ip, r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    def test_rand_int(self):
        num = rand_int()
        self.assertTrue(isinstance(num, int))
        self.assertGreaterEqual(num, 1000)
        self.assertLessEqual(num, 9000)
