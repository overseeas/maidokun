import requests
from base64 import b64encode
import environ
import os
from pathlib import Path
import time

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, 'maidokun/.env'))

headers = "test"
def edit_item(parameters: dict):
    uri = "ttps://circus.shopping.yahooapis.jp/ShoppingWebService/V1/editItem"
    if parameters:
        uri += "?"
        listed_parameter = []
        for key, value in parameters.items():
            listed_parameter.append(key + "=" + value)
        uri += "&".join(listed_parameter)

    r = requests.post(uri, headers= headers)
    time.sleep(0.2)
    if r.status_code == 200:
        return r.json()
    else:
        time.sleep(1)
        print("1 second delayed")
        return items_search(parameters)
