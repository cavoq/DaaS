from fastapi import FastAPI
from src.log import log
from src.routers import layer3, layer4, layer7
import uvicorn
import os
import sys

app = FastAPI(title="denialofservice-api", version="3.0.1")

app.include_router(layer3.layer3_router, prefix="/layer3", tags=["layer3"])
app.include_router(layer4.layer4_router, prefix="/layer4", tags=["layer4"])
app.include_router(layer7.layer7_router, prefix="/layer7", tags=["layer7"])


def start(port: int):
    database_url = os.environ.get(
        "DATABASE_URL", "sqlite:///db/denialofservice.db")
    if os.environ.get("MOCK") == 1:
        database_url = os.environ.get(
            "TEST_DATABASE_URL", "sqlite:///db/denialofservice_test.db")
    log.info(f"Starting server on port {port} with database {database_url}")
    uvicorn.run("server:app", port=port, log_level="info")


if __name__ == "__main__":
    if sys.argv[1] == "container":
        start(int(os.environ["PORT"]))
    elif sys.argv[1] == "direct":
        try:
            start(sys.argv[2], int(sys.argv[3]))
        except:
            log.error("Not able to start server")
