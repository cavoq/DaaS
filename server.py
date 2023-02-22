from fastapi import FastAPI
from log import log
from routers import layer3, layer4, layer7
import uvicorn
import os, sys


app = FastAPI(title="denialofservice-api", version="1.0.1")

app.include_router(layer3.layer3_router, prefix="/layer3", tags=["layer3"])
app.include_router(layer4.layer4_router, prefix="/layer4", tags=["layer4"])
app.include_router(layer7.layer7_router, prefix="/layer7", tags=["layer7"])

def start(host: str, port: int):
    uvicorn.run("server:app", host=host, port=port, log_level="info")
    
if __name__ == "__main__":
    if sys.argv[1] == "container":
        start(os.environ["HOST"], int(os.environ["PORT"]))
    elif sys.argv[1] == "direct":
        try:
            start(sys.argv[2], int(sys.argv[3]))
        except:
            log.error("Not able to start server")
            

