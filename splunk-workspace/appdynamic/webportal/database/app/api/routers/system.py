from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.system import ServiceStatus

router = APIRouter(
    prefix="/api/system",
    tags=["system"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


isService = True


@router.get("/healthcheck")
async def _healthcheck():
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


@router.post("/service")
async def _toggle_service(serviceStatus: ServiceStatus):
    global isService

    if not serviceStatus.state:
        print("Service is Disable")
    else:
        print("Service is Enable")

    isService = serviceStatus.state

    return serviceStatus
