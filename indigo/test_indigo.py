import requests
import json
from sshtunnel import SSHTunnelForwarder


server = SSHTunnelForwarder(
    ('135.181.56.67', 22),
    ssh_username="user",
    ssh_password="Mail123123",
    remote_bind_address=('127.0.0.1', 45000)
)
server.start()

port = server.local_bind_port
url = f'http://127.0.0.1:{port}/api/v2/profile'
r = requests.get(url=url, headers={'accept': 'application/json'})
json_data = json.dumps(r.status_code)
print(json_data)
# for p in json_data:
#     try:
#         name = p['name']
#     except:
#         name = 'null'
#     try:
#         uuid = p['uuid']
#     except TypeError:
#         uuid = ''
#     try:
#         group = p['group']
#     except:
#         group = 'no'
#     try:
#         notes = p['notes']
#     except KeyError:
#         notes = "Null"
#     browser = p['browser']
#     updated = p['updated']

#     print(name, uuid, group, notes, browser, updated)
