import os
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


def get_config():
    config_path = os.environ.get("CONFIG") or "config.json"
    with open(config_path, 'r') as config_file:
        return json.load(config_file)