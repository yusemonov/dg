import os
from dotenv import load_dotenv
from gologin_app.gologin.gologin import GoLogin
from celery import shared_task
from .models import *
load_dotenv('../.env')


@shared_task
def get_profiles_gologin():
    TOKEN_GOLOGIN = os.getenv('TOKEN')
    gl = GoLogin({
        'token': TOKEN_GOLOGIN
    })

    profile_list = gl.profiles()
    for p in profile_list:
        name = p['name']
        role = p['role']
        gologin_id = p['id']
        notes = p['notes']
        browserType = p['browserType']
        lockEnabled = p['lockEnabled']
        timezone = p['timezone']
        navigator = p['navigator']
        language = p['language']
        geolocation = p['geolocation']
        enabled = p['enabled']
        customize = p['customize']
        fillBasedOnIp = p['fillBasedOnIp']
        latitude = p['latitude']
        longitude = p['longitude']
        accuracy = p['accuracy']
        canBeRunning = p['canBeRunning']
        os = p['os']
        proxy = p['proxy']
        host = p['host']
        port = p['port']
        username = p['username']
        password = p['password']
        autoProxyRegion = p['autoProxyRegion']
        torProxyRegion = p['torProxyRegion']
        proxyType = p['proxyType']
        folders = p['folders']
        sharedEmails = p['sharedEmails']
        shareId = p['shareId']
        createdAt = p['createdAt']
        updatedAt = p['updatedAt']
        lastActivity = p['lastActivity']
        if GoProfiles.objects.get(gologin_id=gologin_id).exists():
            continue
        else:
            GoProfiles.objects.create(
                name=name,
                role=role,
                gologin_id=gologin_id,
                notes=notes,
                browserType=browserType,
                lockEnabled=lockEnabled,
                timezone=timezone,
                navigator=navigator,
                language=language,
                geolocation=geolocation,
                enabled=enabled,
                customize=customize,
                fillBasedOnIp=fillBasedOnIp,
                latitude=latitude,
                longitude=longitude,
                accuracy=accuracy,
                canBeRunning=canBeRunning,
                os=os,
                proxy=proxy,
                host=host,
                port=port,
                username=username,
                password=password,
                autoProxyRegion=autoProxyRegion,
                torProxyRegion=torProxyRegion,
                proxyType=proxyType,
                folders=folders,
                sharedEmails=sharedEmails,
                shareId=shareId,
                createdAt=createdAt,
                updatedAt=updatedAt,
                lastActivity=lastActivity,
            )
            return "Добавлен профиль"


# @app.task
# def create_user(username, password):
#     User.objects.create(username=username, password=password)
