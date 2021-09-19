from django.db import models
import requests


class ProfileCreditations(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=700)
    email = models.EmailField(verbose_name='API email')
    token = models.CharField(verbose_name='API Key', max_length=700)
    certtoken = models.TextField(
        verbose_name='API Certkey', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Данные профиля'
        verbose_name_plural = 'Данные профиля'

    def __str__(self):
        return self.name


class NameServers(models.Model):
    name_server_1 = models.CharField(max_length=128)
    name_server_2 = models.CharField(max_length=128)


class ProfileCf(models.Model):
    email_cf = models.EmailField(verbose_name='email')
    token_cf = models.CharField(verbose_name='token', max_length=64)

    def __str__(self):
        return self.email_cf


class Domains(models.Model):
    cf_id = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=700, null=False, blank=True)
    paused = models.CharField(max_length=700, null=False, blank=True)
    type = models.CharField(max_length=700, null=False, blank=True)
    development_mode = models.CharField(max_length=700, null=False, blank=True)
    name_servers_1 = models.TextField(null=False, blank=True)
    name_servers_2 = models.TextField(null=False, blank=True)
    original_name_servers = models.CharField(
        max_length=700, null=False, blank=True)
    original_registrar = models.CharField(
        max_length=700, null=False, blank=True)
    original_dnshost = models.CharField(max_length=700, null=False, blank=True)
    modified_on = models.CharField(max_length=700, null=False, blank=True)
    created_on = models.CharField(max_length=700, null=False,  blank=True)
    activated_on = models.CharField(max_length=700, null=False,  blank=True)
    meta = models.CharField(max_length=700, null=False,  blank=True)
    owner = models.CharField(max_length=700, null=False, blank=True)
    account = models.CharField(max_length=700, null=False,  blank=True)
    permissions = models.CharField(max_length=700, null=False, blank=True)
    plan = models.CharField(max_length=700, null=False, blank=True)

    class Meta:
        verbose_name = 'Домены'
        verbose_name_plural = 'Домены'

# class Domains(models.Model):
    # id = models.CharField(
    #     max_length=700, primary_key=True, null=False)
    # name = models.CharField(max_length=128)
    # status = models.CharField(max_length=700, null=False, blank=True)
    # paused = models.CharField(max_length=700, null=False, blank=True)
    # type = models.CharField(max_length=700, null=False, blank=True)
    # development_mode = models.CharField(max_length=700, null=False, blank=True)
    # name_servers = models.TextField(null=False, blank=True)
    # original_name_servers = models.CharField(
    #     max_length=700, null=False, blank=True)
    # original_registrar = models.CharField(
    #     max_length=700, null=False, blank=True)
    # original_dnshost = models.CharField(max_length=700, null=False, blank=True)
    # modified_on = models.CharField(max_length=700, null=False, blank=True)
    # created_on = models.CharField(max_length=700, null=False,  blank=True)
    # activated_on = models.CharField(max_length=700, null=False,  blank=True)
    # meta = models.CharField(max_length=700, null=False,  blank=True)
    # owner = models.CharField(max_length=700, null=False, blank=True)
    # account = models.CharField(max_length=700, null=False,  blank=True)
    # permissions = models.CharField(max_length=700, null=False, blank=True)
    # plan = models.CharField(max_length=700, null=False, blank=True)
