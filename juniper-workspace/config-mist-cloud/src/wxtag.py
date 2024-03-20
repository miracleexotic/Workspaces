import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getWXTags():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/wxtags"

    resp = requests.get(url=apiUrl, headers=header)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createWXTag(label):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/wxtags"

    body = label

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/WXTags.json") as f:
        data_wxtags = json.load(f)

    for label in data_wxtags:
        createWXTag(label)

    result = getWXTags()
    __import__("pprint").pprint(result)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/WXTags.json") as f:
        data_wxtags = json.load(f)

    for label in data_wxtags:
        createWXTag(label)

    getWXTags()
