import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getSSOProfiles():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/ssos"

    resp = requests.get(url=apiUrl, headers=header)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createSSOProfile(role):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/ssos"

    body = role

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/SSOProfiles.json") as f:
        data_sso_profiles = json.load(f)

    for profile in data_sso_profiles:
        createSSOProfile(profile)

    result = getSSOProfiles()
    __import__("pprint").pprint(result)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/SSOProfiles.json") as f:
        data_sso_profiles = json.load(f)

    for profile in data_sso_profiles:
        createSSOProfile(profile)

    getSSOProfiles()
