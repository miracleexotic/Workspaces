from fastapi import (
    FastAPI,
    status,
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()


@app.get("/healthcheck")
async def home():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            {
                "data": {
                    "status": "UP",
                }
            }
        ),
    )
