"""Test Layer 7 Denial of Service attacks."""

from src.denialofservice.layer7 import Layer7
import threading
import time
import unittest
from scapy.all import *


TEST_DOMAIN = "www.google.com"
TIME = 5
PAYLOAD = '{"data": "test"}'
PORT = 80
MY_IP = "192.168.2.7"


class TestLayer7(unittest.TestCase):

    def test_http_get_flood(self):
        t = threading.Thread(target=Layer7.http_get_flood,
                             args=(TEST_DOMAIN, TIME))
        t.start()
        time.sleep(1)
        packets = sniff(
            timeout=TIME, filter="tcp port 443 and dst host {}".format(TEST_DOMAIN))
        t.join()
        print(packets)
        self.assertGreater(len(packets), 0)

    def test_http_post_flood(self):
        t = threading.Thread(target=Layer7.http_post_flood,
                             args=(TEST_DOMAIN, TIME, PAYLOAD))
        t.start()
        time.sleep(1)
        packets = sniff(
            timeout=TIME, filter="tcp port 443 and dst host {}".format(TEST_DOMAIN))
        t.join()
        self.assertGreater(len(packets), 0)

    def test_slow_loris(self):
        t = threading.Thread(target=Layer7.slow_loris,
                             args=(TEST_DOMAIN, PORT, TIME))
        t.start()
        time.sleep(1)
        packets = sniff(
            timeout=TIME, filter="tcp port 80 and dst host {}".format(TEST_DOMAIN))
        t.join()
        self.assertGreater(len(packets), 0)
