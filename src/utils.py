"""Utils for the project."""

import random
import json
from scapy.all import RandIP


def get_gmail_account_from_file(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
    return data['account'], data['password']


def spoof_ip():
    return str(RandIP())


def rand_int():
    return random.randint(1000, 9000)
