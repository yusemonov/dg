from celery import shared_task
import requests
import json
from .models import IndigoProfile
from sshtunnel import SSHTunnelForwarder


@shared_task
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
    json_data = json.loads(r.text.strip())
    for p in json_data:
        name = p['name']
        uuid = p['uuid']
        try:
            group = p['group']
        except:
            group = 'no'
        try:
            notes = p['notes']
        except KeyError:
            notes = "Null"
        browser = p['browser']
        updated = p['updated']
        if IndigoProfile.objects.filter(uuid=uuid).exists():
            continue
        else:

            IndigoProfile.objects.create(
                name=name, uuid=uuid, group=group, notes=notes, browser=browser, updated=updated, is_add=True)
            return "Добавлен профиль"


# @app.task
# def create_user(username, password):
#     User.objects.create(username=username, password=password)
