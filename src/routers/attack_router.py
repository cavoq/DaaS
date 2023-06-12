import json
from fastapi import APIRouter, Depends, Request, Response
from src.auth import verify_api_key
from src.controllers.attack_controller import attack_controller

attack_router = APIRouter()


@attack_router.get("/status/{attack_id}")
async def get_attack_status(attack_id: str, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    attack = attack_controller.get_attack(attack_id)
    if attack is None:
        return Response(status_code=404, content=json.dumps({"status": "Attack not found"}), media_type="application/json")
    status = attack.get_status()
    return Response(status_code=200, content=status, media_type="application/json")


@attack_router.get("/stop/{attack_id}")
async def stop_attack(attack_id: str, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    attack = attack_controller.get_attack(attack_id)
    if attack is None:
        return Response(status_code=404, content=json.dumps({"status": "Attack not found"}), media_type="application/json")
    attack.stop()
    return Response(status_code=200, content=json.dumps({"status": "Attack stopped"}), media_type="application/json")


@attack_router.get("/delete/{attack_id}")
async def delete_attack(attack_id: str, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    deleted = attack_controller.delete_attack(attack_id)
    if not deleted:
        return Response(status_code=404, content=json.dumps({"status": "Attack not found"}), media_type="application/json")
    return Response(status_code=200, content=json.dumps({"status": "Attack deleted"}), media_type="application/json")
