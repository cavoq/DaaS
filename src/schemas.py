from pydantic import BaseModel


class Layer4FloodRequest(BaseModel):
    target: str
    port: int
    time: int


class ICMPFloodRequest(BaseModel):
    target: str
    time: int


class EmailSpamRequest(BaseModel):
    target: str
    time: int
    message: str


class HttpGetFloodRequest(BaseModel):
    target: str
    time: int
    port: int


class HttpPostFloodRequest(BaseModel):
    target: str
    time: int
    port: int
    payload: str


class SlowlorisFloodRequest(BaseModel):
    target: str
    time: int
    port: int
