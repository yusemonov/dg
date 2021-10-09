import CloudFlare
import configparser
config = configparser.ConfigParser()

# cf = CloudFlare.CloudFlare(email='whitetech.lp@gmail.com', token='ff029fbbc9b791bac44bba34f88b3738bea3f')
# zones = cf.zones.get()
# for zone in zones:
# print(zone['id'])

# name = zone['name']
# status = zone['status']
# paused = zone['paused']
# type = zone['type']
# development_mode = zone['development_mode']
# name_servers = zone['name_servers']
# original_name_servers = zone['original_name_servers']
# original_registrar = zone['original_registrar']
# original_dnshost = zone['original_dnshost']
# modified_on = zone['modified_on']
# created_on = zone['created_on']
# activated_on = zone['activated_on']
# meta = zone['meta']
# owner = zone['owner']
# account = zone['account']
# permissions = zone['permissions']
# print(original_registrar)
# Domains.objects.create(name=name,
#                        status=status,
#                        paused=paused,
#                        type=type,
#                        development_mode=development_mode,
#                        name_servers=name_servers,
#                        original_name_servers=original_name_servers,
#                        original_registrar=original_registrar,
#                        original_dnshost=original_dnshost,
#                        modified_on=modified_on,
#                        created_on=created_on,
#                        activated_on=activated_on,
#                        meta=meta,
#                        owner=owner,
#                        account=account,
#                        permissions=permissions
#                        )
