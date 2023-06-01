from fastapi import Depends, FastAPI, Request, Form, security
from sqladmin import Admin
from dotenv import load_dotenv
from src.log import log
from src.db import Database
from src.auth import authenticate_user
from src.admin_views import ApiKeyAdmin, AttackAdmin
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi.responses import HTMLResponse
from src.routers import layer3, layer4, layer7, attack_router
import uvicorn
import os
import sys


load_dotenv()

app = FastAPI(title="DaaS", version="3.0.1")
security = HTTPBasic()

app.include_router(layer3.layer3_router, prefix="/layer3", tags=["layer3"])
app.include_router(layer4.layer4_router, prefix="/layer4", tags=["layer4"])
app.include_router(layer7.layer7_router, prefix="/layer7", tags=["layer7"])
app.include_router(attack_router.attack_router,
                   prefix="/attacks", tags=["attacks"])

if os.environ.get("MOCK") == "1":
    database_url = os.environ.get("TEST_DATABASE_URL")
else:
    database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    log.error("No database url found")
    exit(1)
Database(database_url)


@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    username = await authenticate_user(credentials)
    return {"redirect": "/admin"}


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    with open("resources/login.html", "r") as login_page:
        return login_page.read()


admin = Admin(app, Database.get_engine(), debug=True, base_url="/admin")

admin.add_model_view(ApiKeyAdmin)
admin.add_model_view(AttackAdmin)

app.mount("/admin", admin.app)

if __name__ == "__main__":
    if sys.argv[1] == "container":
        uvicorn.run("server:app", port=int(
            os.environ.get("PORT")), log_level="info")
    elif sys.argv[1] == "direct":
        try:
            uvicorn.run("server:app", port=int(sys.argv[2]), log_level="info")
        except Exception as error:
            log.error(f"Not able to start server {error}")
