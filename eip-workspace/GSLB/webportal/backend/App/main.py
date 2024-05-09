from fastapi import (
    FastAPI,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class ServiceStatus(BaseModel):
    state: bool


isService = True

app = FastAPI()

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
