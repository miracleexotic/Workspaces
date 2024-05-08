import requests
import dotenv
import json

config = dotenv.dotenv_values()
API_HOST = config["API_HOST"]
API_TOKEN = config["API_TOKEN"]
ORG_ID = config["ORG_ID"]


def getWLANTemplates():
    header = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/templates"

    resp = requests.get(url=apiUrl, headers=header)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createWLANTemplate(template):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/templates"

    body = template

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def getWLANSSIDs():
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/wlans"

    resp = requests.get(url=apiUrl, headers=headers)
    # __import__("pprint").pprint(resp.json())

    return resp.json()


def createWLANSSID(ssid):
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    apiUrl = f"https://{API_HOST}/api/v1/orgs/{ORG_ID}/wlans"

    body = ssid

    resp = requests.post(url=apiUrl, headers=headers, json=body)
    # __import__("pprint").pprint(resp.json())

    return resp.json()["id"]


def run():
    with open("../Templates/WLANs.json") as f:
        data_wlans = json.load(f)

    for wlan in data_wlans:
        template_id = createWLANTemplate(wlan["template"])
        for ssid in wlan["wlans"]:
            ssid["template_id"] = template_id
            createWLANSSID(ssid)

    result_templates = getWLANTemplates()
    __import__("pprint").pprint(result_templates)

    result_ssid = getWLANSSIDs()
    __import__("pprint").pprint(result_ssid)


if __name__ == "__main__":
    print("TOKEN:", API_TOKEN)
    print("OGR:", ORG_ID)

    with open("../Templates/WLANs.json") as f:
        data_wlans = json.load(f)

    for wlan in data_wlans:
        template_id = createWLANTemplate(wlan["template"])
        for ssid in wlan["wlans"]:
            ssid["template_id"] = template_id
            createWLANSSID(ssid)

    getWLANTemplates()
    getWLANSSIDs()
