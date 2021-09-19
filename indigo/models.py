from django.contrib.auth.models import User
from django.db import models


class IndigoProfile(models.Model):
    CHOICES_BROWSER = (
        ('mimic', 'mimic'),
        ('stealthfox', 'stealthfox'),
        ('mimic_mobile', 'mimic_mobile')
    )
    CHOICES_OS = (
        ('win', 'win'),
        ('mac', 'mac'),
        ('linux', 'linux'),
        ('android', 'android'),
    )

    uuid = models.CharField(max_length=255, blank=True)
    group = models.CharField(
        'IndigoGroup', max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    notes = models.TextField(max_length=2048, blank=True, default='notes')
    browser = models.CharField(
        choices=CHOICES_BROWSER, max_length=20, default='mimic')
    updated = models.CharField('updated', max_length=255, blank=True)
    browserNeedsUpdate = models.BooleanField(default=True)
    os = models.CharField(choices=CHOICES_OS, max_length=10, default='win')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    network = models.ForeignKey(
        'ListsProxy', blank=True, null=True, on_delete=models.SET_NULL)
    is_add = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Профили индиго'
        verbose_name_plural = 'Профили индиго'

    def __str__(self):
        return self.name


class ListsProxy(models.Model):
    PROTOCOL_TYPES = (
        ('NONE', 'none'),
        ('HTTP', 'http'),
        ('SOCKS', 'socks'),
    )
    proxy_type = models.CharField(
        choices=PROTOCOL_TYPES, max_length=10, default='HTTP')
    ip = models.CharField('Host', max_length=20, default='127.0.0.1')
    port = models.IntegerField('Port', default='1080')
    protocol = models.CharField('protocol', max_length=20, default='SOCKS5')
    anonymity = models.CharField('anonymity', max_length=20, blank=True)
    https = models.BooleanField('https', null=True, default=False)
    country = models.CharField('country', max_length=255, default='empty')
    city = models.CharField('city', max_length=255, default='empty')
    proxy_username = models.CharField(
        max_length=20, blank=True, null=True)
    proxy_password = models.CharField(
        'Password', max_length=50, null=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Прокси лист'
        verbose_name_plural = 'Прокси лист'


class Gologin(models.Model):
    profile_id = models.CharField(max_length=255)
