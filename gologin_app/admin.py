from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(GoProfiles)
class GoProfilesAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'role',
                    'gologing_id',
                    'notes',
                    'browserType',
                    'lockEnabled',
                    'timezone',
                    'timezone',
                    'navigator',
                    'language',
                    'geolocation',
                    'enabled',
                    'customize',
                    'fillBasedOnIp',
                    'latitude',
                    'longitude',
                    'accuracy',
                    'canBeRunning',
                    'os',
                    'proxy',
                    'host',
                    'port',
                    'username',
                    'password',
                    'autoProxyRegion',
                    'torProxyRegion',
                    'proxyType',
                    'folders',
                    'sharedEmails',
                    'shareId',
                    'createdAt',
                    'updatedAt',
                    'lastActivity',)
