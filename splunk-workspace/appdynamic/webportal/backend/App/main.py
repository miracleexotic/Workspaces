from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from App.schemas.system import ServiceStatus
import httpx
from dotenv import dotenv_values

config = dotenv_values("App/.env")


app = FastAPI()

isService = True


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
async def home():
    global isService
    return JSONResponse(
        status_code=(
            status.HTTP_200_OK if isService else status.HTTP_504_GATEWAY_TIMEOUT
        ),
        content=jsonable_encoder(
            {
                "data": {
                    "status": "UP" if isService else "DOWN",
                    "state": isService,
                }
            }
        ),
    )


@app.post("/service")
async def toggle_service(serviceStatus: ServiceStatus):
    global isService

    if not serviceStatus.state:
        print("Service is Disable")
    else:
        print("Service is Enable")

    isService = serviceStatus.state

    return serviceStatus


@app.get("/database")
async def database():
    print(config["BACKEND_DB_URL"])
    async with httpx.AsyncClient() as client:
        url = f"{config['BACKEND_DB_URL']}/healthcheck"
        resp = await client.get(url)

        data = resp.json()

        return JSONResponse(
            status_code=resp.status_code,
            content=jsonable_encoder(
                {
                    "data": {
                        "status": data["data"]["status"],
                        "state": data["data"]["state"],
                    }
                }
            ),
        )
