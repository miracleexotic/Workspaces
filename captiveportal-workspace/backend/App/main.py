from fastapi import (
    FastAPI,
    status,
    APIRouter,
    Depends,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from .Cloudflare import validate_cloudflare, POLICY_AUD, CERTS_URL

from dotenv import dotenv_values
import urllib.parse
import base64
import time
import hashlib
import hmac
import httpx


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(validate_cloudflare)],
    responses={404: {"description": "Not found"}},
)

config = dotenv_values(".env")
API_VERSION = config["API_VERSION"]
MIST_KEY = config["MIST_KEY"]


class Data(BaseModel):
    Email: str | None = None
    Firstname: str | None = None
    Lastname: str | None = None
    Company: str | None = None
    Ap_mac: str | None = None
    Ap_name: str | None = None
    Authorize_url: str | None = None
    Site_name: str | None = None
    Ssid: str | None = None
    Wlan_id: str | None = None
    Client_mac: str | None = None
    Url: str | None = None
    Authorize_min: int | None = 525600
    Download_kbps: int | None = 0
    Upload_kbps: int | None = 0
    Quota_mbytes: int | None = 0


@app.get("/")
async def home():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            {
                "data": {
                    "status": "UP",
                    "juniperMist": {"apiVer": API_VERSION, "mistKey": MIST_KEY},
                    "cloudflare": {"policyAUD": POLICY_AUD, "certUrl": CERTS_URL},
                }
            }
        ),
    )


@router.post(f"{API_VERSION}/auth/juniper")
async def auth_juniper(data: Data):
    print(data)
    context = f"{data.Wlan_id}/{data.Ap_mac}/{data.Client_mac}/{data.Authorize_min}/{data.Download_kbps}/{data.Upload_kbps}/{data.Quota_mbytes}"
    context_b64 = base64.b64encode(context.encode("ascii")).decode("ascii")
    token = urllib.parse.quote_plus(context_b64)

    payload = {
        "expires": int(time.time()) + 120,
        "token": token,
        "forward": str(urllib.parse.quote_plus(str(data.Url))),
        "name": f"{data.Firstname} {data.Lastname}",
        "email": str(data.Email),
        "company": str(data.Company),
        "field1": "",
        "field2": "",
        "field3": "",
        "field4": "",
    }
    print("b64:", context_b64)
    print("token: ", token)
    print(payload)

    hash_hmac = hmac.new(
        MIST_KEY.encode(), urllib.parse.urlencode(payload).encode(), hashlib.sha1
    ).digest()
    hash_hmac_b64 = base64.b64encode(hash_hmac).decode("ascii")
    signature = urllib.parse.quote_plus(hash_hmac_b64)
    print("hash_hmac:", hash_hmac)
    print("hash_hmac_b64:", hash_hmac_b64)
    print("signature:", signature)

    final_url = f"{urllib.parse.unquote_plus(str(data.Authorize_url))}?signature={signature}&{urllib.parse.urlencode(payload)}"

    async with httpx.AsyncClient() as client:
        r = await client.get(final_url)

    print(r.content)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({"data": {"url": final_url}}),
    )


app.include_router(router)
