from celery import shared_task
from dolphin.models import DolphinInfo
import requests


@shared_task
def get_dolphin_info():
    url = "https://finnyheder.com/new/accounts/"

    payload = ""
    headers = {
        'Authorization': '1-c1df40635d8ee80097645ec1e003c99e',
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload).json()
    for d in response['data']:
        dolphin_id = d['id']
        user_id = d['user_id']
        group_id = d['group_id']
        proxy_id = d['proxy_id']
        name = d['name']
        notes = d['notes']
        # tags = d['tags']
        permissions = d['permissions']
        user_agent = d['user_agent']
        access_token = d['access_token']
        business_access_token = d['business_access_token']
        login = d['login']
        password = d['password']
        if DolphinInfo.objects.filter(id=dolphin_id).exists():
            continue
        else:
            DolphinInfo.objects.create(dolphin_id=dolphin_id, user_id=user_id, group_id=group_id,
                                       proxy_id=proxy_id, name=name, notes=notes, user_agent=user_agent, access_token=access_token, business_access_token=business_access_token, login=login, password=password)


