from fastapi import Header, HTTPException
from datetime import datetime

import pytz
from src.db import Database
from src.models import ApiKey


async def verify_api_key(api_key: str = Header(None)):
    now_utc = datetime.now(pytz.utc)

    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")

    session = Database.get_session()

    api_key: ApiKey = session.query(ApiKey).filter_by(key=api_key).first()
    
    if api_key is None:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    ts_created_utc = api_key.ts_created.astimezone(pytz.utc)
    ts_expired_utc = api_key.ts_expired.astimezone(pytz.utc)

    session.close()

    if now_utc < ts_created_utc or now_utc > ts_expired_utc:
        raise HTTPException(status_code=401, detail="API key expired")

    return True
