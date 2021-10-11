import json
import os
import requests
from dotenv import load_dotenv
# load dotenv
load_dotenv('../.env')

BASE_URL = os.getenv('BASE_URL')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


def check_token(baseUrl=BASE_URL, authToken=AUTH_TOKEN):
    url = f"https://{baseUrl}/new/accounts/check_token/"

    payload = ""
    headers = {
        'Authorization': f'{authToken}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


check_token()
