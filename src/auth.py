"""Module for authentication and authorization."""

from fastapi import Header, HTTPException
from datetime import datetime

from src.models import ApiKey


async def verify_api_key(api_key: str = Header(None)):
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")

    api_key: ApiKey = ApiKey.query.filter_by(key=api_key).first()
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")

    now = datetime.utcnow()
    if now < api_key.ts_created or now > api_key.ts_expired:
        raise HTTPException(status_code=401, detail="API key expired")

    return True
