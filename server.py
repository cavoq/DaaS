from fastapi import FastAPI
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.log import log
from src.models import Base
from src.routers import layer3, layer4, layer7
import uvicorn
import os
import sys

app = FastAPI(title="denialofservice-api", version="3.0.1")

app.include_router(layer3.layer3_router, prefix="/layer3", tags=["layer3"])
app.include_router(layer4.layer4_router, prefix="/layer4", tags=["layer4"])
app.include_router(layer7.layer7_router, prefix="/layer7", tags=["layer7"])


def setup_db():
    if os.environ.get("MOCK") == "1":
        database_url = os.environ.get("TEST_DATABASE_URL")
    else:
        database_url = os.environ.get("DATABASE_URL")
    if database_url is None:
        log.error("No database url found")
        exit(1)
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)


def start(port: int):
    load_dotenv()
    setup_db()
    uvicorn.run("server:app", port=port, log_level="info")


if __name__ == "__main__":
    if sys.argv[1] == "container":
        start(int(os.environ["PORT"]))
    elif sys.argv[1] == "direct":
        try:
            start(int(sys.argv[2]))
        except:
            log.error("Not able to start server")
