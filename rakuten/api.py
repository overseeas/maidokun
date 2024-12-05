import requests
from base64 import b64encode
import environ
import os
from pathlib import Path
import time

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, 'maidokun/.env'))

def add_auth_to_header(header: dict):
    header['Authorization'] = 'ESA ' + str(b64encode((env('SERVICE_SECRET') + ':' + env('LICENSE_KEY')).encode("utf-8")), "utf-8")
    return header

def items_search(parameters: dict):
    uri = "https://api.rms.rakuten.co.jp/es/2.0/items/search"
    if parameters:
        uri = uri + "?"
        for key, value in parameters.items():
            uri = uri + key + "=" + value + "&"

    headers = add_auth_to_header(dict())

    
    r = requests.get(uri, headers= headers)
    time.sleep(0.2)
    if r.status_code == 200:
        return r.json()
    else:
        time.sleep(1)
        print("1 second delayed")
        return items_search(parameters)
