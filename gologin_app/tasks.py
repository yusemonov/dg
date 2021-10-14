import os
from gologin_app.gologin.gologin import GoLogin
from celery import shared_task
from .models import *
import json


@shared_task
def get_profiles_gologin():
    gl = GoLogin({
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGU0NjBhZGQyMDk3OWYyZmEwNmE2ZDEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTY0MGFhZjAyMmUxYTI1ZTcyZjA0NmUifQ.6L85fs-NvcqnvxluRDrDHexMKqkWTO0KHGUYMzbW6Og'})

    json_data = gl.profiles()
    for x in json_data:
        name = x['name']
        role = x['role']
        gologing_id = x['id']
        notes = x['notes']
        browserType = x['browserType']
        lockEnabled = x['lockEnabled']
        timezone = x['timezone']
        navigator = x['navigator']
        geolocation = x['geolocation']
        canBeRunning = x['canBeRunning']
        os = x['os']
        proxy = x['proxy']
        try:
            proxyType = x['proxyType']
        except KeyError:
            proxyType = 'NULL'
        try:
            folders = x['folders']
        except:
            folders = 'NULL'
        sharedEmails = x['sharedEmails']
        shareId = x['shareId']
        createdAt = x['createdAt']
        updatedAt = x['updatedAt']
        try:
            lastActivity = x['lastActivity']
        except:
            lastActivity = 'NULL'
        if GoProfiles.objects.filter(gologing_id=gologing_id).exists():
            continue
        else:
            GoProfiles.objects.create(
                name=name,
                role=role,
                gologing_id=gologing_id,
                notes=notes,
                browserType=browserType,
                lockEnabled=lockEnabled,
                timezone=timezone,
                navigator=navigator,
                geolocation=geolocation,
                canBeRunning=canBeRunning,
                os=os,
                proxy=proxy,
                proxyType=proxyType,
                folders=folders,
                sharedEmails=sharedEmails,
                shareId=shareId,
                createdAt=createdAt,
                updatedAt=updatedAt,
                lastActivity=lastActivity,
            )


@shared_task
def crear_db_gologin():
    for gologing_id in GoProfiles.objects.values_list('gologing_id', flat=True).distinct():
        GoProfiles.objects.filter(pk__in=GoProfiles.objects.filter(
            gologing_id=gologing_id).values_list('id', flat=True)[3:]).delete()
