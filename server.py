from fastapi import FastAPI
from routers import Layer3, Layer4, Layer7
import uvicorn
import os

app = FastAPI()

app.include_router(Layer3.router, prefix="/Layer3")
app.include_router(Layer4.router, prefix="/Layer4")
app.include_router(Layer7.router, prefix="/Layer7")

def start():
    uvicorn.run("server:app", host=os.environ["HOST"], port=os.environ["PORT"], log_level="info")
    
if __name__ == "__main__":
    start()
