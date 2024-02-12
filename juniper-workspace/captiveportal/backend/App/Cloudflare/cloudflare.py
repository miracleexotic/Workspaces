from fastapi import Request, HTTPException
import requests
import json
import jwt
from dotenv import dotenv_values


config = dotenv_values(".env")

# The Application Audience (AUD) tag for your application
POLICY_AUD = config["POLICY_AUD"]

# Your CF Access team domain
TEAM_DOMAIN = config["TEAM_DOMAIN"]
CERTS_URL = config["CERTS_URL"]


async def validate_cloudflare(request: Request):
    """
    Validate that the request is authenticated by Cloudflare Access.
    """
    if not verify_token(request):
        raise HTTPException(status_code=400, detail="Not authenticated properly!")


def _get_public_keys():
    """
    Returns:
        List of RSA public keys usable by PyJWT.
    """
    r = requests.get(str(CERTS_URL))
    public_keys = []
    jwk_set = r.json()
    for key_dict in jwk_set["keys"]:
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key_dict))
        public_keys.append(public_key)
    return public_keys


def verify_token(request):
    """
    Verify the token in the request.
    """
    token = ""

    if "CF_Authorization" in request.cookies:
        token = request.cookies["CF_Authorization"]
    else:
        raise HTTPException(
            status_code=400, detail="missing required cf authorization token"
        )

    keys = _get_public_keys()

    # Loop through the keys since we can't pass the key set to the decoder
    valid_token = False
    for key in keys:
        try:
            # decode returns the claims that has the email when needed
            jwt.decode(token, key=key, audience=POLICY_AUD, algorithms=["RS256"])
            valid_token = True
            break
        except Exception as e:
            # Cannot raise at this moment cause some key is correct.
            # But if first key is not correct. It raise and not verify by next key.
            #
            # >>> raise HTTPException(status_code=400, detail=f"Error decoding token: {e}")
            #
            # Need to log some key verify fail.
            print(f"Error decoding token[{key}]: {e}")

    if not valid_token:
        raise HTTPException(status_code=400, detail="Invalid token")

    return True
