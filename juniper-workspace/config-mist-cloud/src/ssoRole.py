import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getSSORoles():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/ssoroles"

    resp = requests.get(url=apiUrl, headers=header)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createSSORole(role):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/ssoroles"

    body = role

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/SSORoles.json") as f:
        data_sso_roles = json.load(f)

    for role in data_sso_roles:
        createSSORole(role)

    result = getSSORoles()
    __import__("pprint").pprint(result)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/SSORoles.json") as f:
        data_sso_roles = json.load(f)

    for role in data_sso_roles:
        createSSORole(role)

    getSSORoles()
