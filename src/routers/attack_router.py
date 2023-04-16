from fastapi import APIRouter, Depends, Request, Response
from src.auth import verify_api_key
from src.controllers.attack_controller import attack_controller

attack_router = APIRouter()


@attack_router.get("/status/{attack_id}")
async def get_attack_status(attack_id: str, request: Request, api_key_dependency: bool = Depends(verify_api_key)):
    status = attack_controller.get_attack(attack_id).get_status()
    return Response(status_code=200, content=status, media_type="application/json")
