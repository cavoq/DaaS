"""Test Layer 4 Denial of Service attacks."""

import threading
import time
import unittest
from scapy.all import sniff
from src.denialofservice.layer4 import Layer4


TARGET_IP = "192.168.2.1"
TARGET_PORT = 80
IFACE = "enp3s0"
TIME = 5


class TestLayer4(unittest.TestCase):

    def test_syn_flood(self):
        sniffed_packets = []
        t = threading.Thread(target=Layer4.syn_flood,
                             args=(TARGET_IP, TARGET_PORT, TIME))
        t.start()
        time.sleep(0.1)
        sniffed_packets = sniff(
            filter='tcp and dst port 80', timeout=TIME, iface=IFACE)
        self.assertGreater(len(sniffed_packets), 0)

    def test_udp_flood(self):
        sniffed_packets = []
        t = threading.Thread(target=Layer4.udp_flood,
                             args=(TARGET_IP, TARGET_PORT, TIME))
        t.start()
        time.sleep(0.1)
        sniffed_packets = sniff(
            filter='udp and dst port 80', timeout=TIME, iface=IFACE)
        self.assertGreater(len(sniffed_packets), 0)
