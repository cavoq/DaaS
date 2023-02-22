import unittest
from scapy.all import sniff
from denialofservice.layer3 import Layer3
import threading


TARGET_IP = "192.168.2.1"


class TestLayer3(unittest.TestCase):
    def test_icmp_flood(self):
        time = 5
        packets = []
        def capture_packets():
            nonlocal packets
            packets = sniff(filter="icmp", timeout=time, iface="enp3s0")
        capture_thread = threading.Thread(target=capture_packets)
        capture_thread.start()
        Layer3.icmp_flood(TARGET_IP, 10)
        capture_thread.join()
        self.assertGreater(len(packets), 1, "ICMP flood test failed")
