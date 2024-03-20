import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getSites():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/sites"

    resp = requests.get(url=apiUrl, headers=header)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createSite(site):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/sites"

    body = site

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/Sites.json") as f:
        data_sites = json.load(f)

    for site in data_sites:
        createSite(site)

    result = getSites()
    __import__("pprint").pprint(result)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/Sites.json") as f:
        data_sites = json.load(f)

    for site in data_sites:
        createSite(site)

    getSites()
