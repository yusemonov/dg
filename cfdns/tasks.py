from __future__ import absolute_import
from celery import shared_task
from .models import Domains


import CloudFlare


@shared_task
def make_published():
    cf = CloudFlare.CloudFlare(
        email='whitetech.lp@gmail.com', token='ff029fbbc9b791bac44bba34f88b3738bea3f')
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
        owner = zone['owner']['email']
        account = zone['account']
        permissions = zone['permissions']
        if Domains.objects.filter(cf_id=id).exists():
            continue
        else:
            Domains.objects.update_or_create(cf_id=id, name=name,
                                             status=status, paused=paused, type=type, owner=owner, name_servers_1=name_servers_1, name_servers_2=name_servers_2)
        return "Добавлен профиль"

        # updated = queryset.update(name=name)
        # self.message_user(request, updated, messages.SUCCESS)

        # Domains.objects.create(name=name,
        #  status=status,
        #  paused=paused,
        #  type=type,
        #  development_mode=development_mode,
        #  name_servers=name_servers,
        #  original_name_servers=original_name_servers,
        #  original_registrar=original_registrar,
        #  original_dnshost=original_dnshost,
        #  modified_on=modified_on,
        #  created_on=created_on,
        #  activated_on=activated_on,
        #  meta=meta,
        #  owner=owner,
        #  account=account,
        #  permissions=permissions
        #    )


@shared_task
def crear_db():
    for name in Domains.objects.values_list('name', flat=True).distinct():
        Domains.objects.filter(pk__in=Domains.objects.filter(
            name=name).values_list('id', flat=True)[3:]).delete()
