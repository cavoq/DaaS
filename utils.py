import random
from scapy.all import RandIP


def get_gmail_account_from_file(path: str):
    file = open(path, "r")
    account = file.readline()
    password = file.readline()
    return account, password


def spoof_ip():
    return RandIP()


def rand_int():
    return random.randint(1000, 9000)
