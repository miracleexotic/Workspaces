from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.system import ServiceStatus
import pymysql
from app.config import settings

router = APIRouter(
    prefix="/api/system",
    tags=["system"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


isService = True


@router.get("/healthcheck")
async def _healthcheck():
    global isService

    with pymysql.connect(
        host=settings.db_ipaddress,
        user=settings.db_username,
        password=settings.db_password,
        database=settings.db_database,
        port=settings.db_port,
    ) as connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user"
            cursor.execute(sql)
            result = cursor.fetchall()

    return JSONResponse(
        status_code=(
            status.HTTP_200_OK if isService else status.HTTP_504_GATEWAY_TIMEOUT
        ),
        content=jsonable_encoder(
            {
                "data": {
                    "status": "UP" if isService else "DOWN",
                    "state": isService,
                    "sql": {"query": sql, "result": result},
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
