import requests
from celery import shared_task
import requests
import json
from sshtunnel import SSHTunnelForwarder


def get_indigo_profiles():
    server = SSHTunnelForwarder(
        ('135.181.56.67', 22),
        ssh_username="user",
        ssh_password="Mail123123",
        remote_bind_address=('127.0.0.1', 45000)
    )
    server.start()

    port = server.local_bind_port

    r = requests.get(
        f'http://127.0.0.1:{port}/api/v2/profile', headers={'accept': 'application/json'})
    json_data = json.dumps(r)
    for p in json_data:
        name = p['name']
        uuid = p['uuid']
        group = p['group']
        group = 'no'
        notes = p['notes']
        notes = "Null"
        browser = p['browser']
        updated = p['updated']
        print(name)
    # if IndigoProfile.objects.filter(uuid=uuid).exists():
    #     continue
    # else:

    #     IndigoProfile.objects.create(
    #         name=name, uuid=uuid, group=group, notes=notes, browser=browser, updated=updated, is_add=True)
    #     return "Добавлен профиль"
get_indigo_profiles()
