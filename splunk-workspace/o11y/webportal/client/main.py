import requests
import random
import time
from datetime import datetime
from dotenv import dotenv_values
from fake_useragent import UserAgent
from urllib3.exceptions import InsecureRequestWarning

# Ignore InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ua = UserAgent()

config = dotenv_values(".env")
URL = config["URL"]

while True:
    ua_selected = ua.random

    resp = requests.get(
        url=URL,
        headers={"User-Agent": ua_selected},
        verify=False,
    )

    print(f"{datetime.ctime(datetime.now())}: [{resp.status_code}] {ua_selected}")

    time.sleep(random.randint(2, 10))
