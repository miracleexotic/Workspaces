import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getSiteGroups():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/sitegroups"

    resp = requests.get(url=apiUrl, headers=header)
    # print(resp.json())

    return resp.json()


def createSiteGroup(group):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/sitegroups"

    body = group

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # print(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/SiteGroups.json") as f:
        data_site_groups = json.load(f)

    for group in data_site_groups:
        createSiteGroup(group)

    result = getSiteGroups()
    __import__("pprint").pprint(result)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/SiteGroups.json") as f:
        data_site_groups = json.load(f)

    for group in data_site_groups:
        createSiteGroup(group)

    getSiteGroups()
