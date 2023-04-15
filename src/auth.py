import os
from fastapi import Header, HTTPException
from datetime import datetime
from src.db import Database
from src.models import ApiKey


async def verify_api_key(api_key: str = Header(None)):
    if os.environ.get("MOCK") == "1": ## This is for testing purposes
        return True
    
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")

    session = Database.get_session()
    api_key: ApiKey = session.query(ApiKey).filter_by(key=api_key).first()
    session.close()
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")

    now = datetime.utcnow()
    if now < api_key.ts_created or now > api_key.ts_expired:
        raise HTTPException(status_code=401, detail="API key expired")

    return True
