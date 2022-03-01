from fastapi import FastAPI
from routers import Layer3, Layer4, Layer7
import uvicorn

app = FastAPI()

app.include_router(Layer3.router, prefix="/Layer3")
app.include_router(Layer4.router, prefix="/Layer4")
app.include_router(Layer7.router, prefix="/Layer7")

def run(host, port):
    uvicorn.run("server:app", host=host, port=port, log_level="info")
