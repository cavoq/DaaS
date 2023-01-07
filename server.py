from fastapi import FastAPI
from log import log
from routers import Layer3, Layer4, Layer7
import uvicorn
import os, sys


app = FastAPI(title="denialofservice-API", version="1.0")

app.include_router(Layer3.router, prefix="/Layer3", tags=["Layer3"])
app.include_router(Layer4.router, prefix="/Layer4", tags=["Layer4"])
app.include_router(Layer7.router, prefix="/Layer7", tags=["Layer7"])

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
            

