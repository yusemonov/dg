from gologin.gologin import GoLogin
from dotenv import load_dotenv
import json
import os
import requests
import logging

load_dotenv('../.env')
TOKEN_GOLOGIN = os.getenv('TOKEN_GOLOGIN')
api = GoLogin({
    'token': TOKEN_GOLOGIN,
    'tmpdir': 'dirs',
})


def create_account(num, suffix):
    options = {
        "name": f"{suffix}_{num}",
        "os": "win",
        "proxy_mode": 'http',
        # "proxy_host": f"{proxy.ip.split(':')[0]}",
        # "proxy_port": f"{proxy.ip.split(':')[1]}",
        # "proxy_username": f"{proxy.login}",
        # "proxy_password": f"{proxy.password}"
    }
    profile_id = api.create(options)
    print(profile_id)
# def add_cookies():
#     print(api.downloadProfileZip())


if __name__ == '__main__':
    create_account(1, 'TEST')
