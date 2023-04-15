import unittest
from scapy.all import sniff
from src.denialofservice.layer3 import Layer3
import threading


TARGET_IP = "192.168.2.1"
TIME = 5
IFACE = "enp3s0"


class TestLayer3(unittest.TestCase):

    def test_icmp_flood(self):
        packets = []

        def capture_packets():
            nonlocal packets
            packets = sniff(filter="icmp", timeout=TIME, iface=IFACE)

        capture_thread = threading.Thread(target=capture_packets)
        capture_thread.start()
        Layer3.icmp_flood(TARGET_IP, TIME)
        capture_thread.join()
        self.assertGreater(len(packets), 1, "ICMP flood test failed")
