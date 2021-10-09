import configparser
import CloudFlare
config = configparser.ConfigParser()
config.read('example.ini')
email = config['white']['email']
token = config['white']['token']

cf = CloudFlare.CloudFlare(email=email, token=token)
zones = cf.zones.get()
for zone in zones:
    id = zone['id']
    name = zone['name']
    status = zone['status']
    paused = zone['paused']
    type = zone['type']
    development_mode = zone['development_mode']
    name_servers_1 = zone['name_servers'][0]
    name_servers_2 = zone['name_servers'][1]
    original_name_servers = zone['original_name_servers']
    original_registrar = zone['original_registrar']
    original_dnshost = zone['original_dnshost']
    modified_on = zone['modified_on']
    created_on = zone['created_on']
    activated_on = zone['activated_on']
    meta = zone['meta']
    owner = zone['owner']
    account = zone['account']
    permissions = zone['permissions']

    print(permissions)
