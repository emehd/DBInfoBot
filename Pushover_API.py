import json
import os
import requests


def send_infos(message):
    url = "https://api.pushover.net/1/messages.json"

    payload = json.dumps({
        "token": os.environ.get("PUSHOVERTOKEN"),
        "user": os.environ.get("PUSHOVERUSER"),
        "message": message
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)