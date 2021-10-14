from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.query_utils import Q
from dolphin.models import DolphinInfo


class AccountFarming(models.Model):
    farmer = models.CharField(verbose_name='Фармер', max_length=128)
    fb_account = models.CharField(verbose_name='Аккаунт', max_length=128)

    class Meta:
        verbose_name = 'фарм'
        verbose_name_plural = 'фарм'

    def __str__(self):
        return self.farmer


class StatusFarm(models.Model):
    status_farm = models.CharField(verbose_name='Статус фарма', max_length=50)

    def __str__(self):
        return self.status_farm


class FarmStages(models.Model):
    stages = models.CharField(
        verbose_name='Статус Фарма', max_length=20)

    def __str__(self):
        return self.stages


class FarmSheets(models.Model):
    status = models.CharField(verbose_name='Статус',
                              max_length=255, null=True, blank=True)
    f_name = models.CharField(
        verbose_name='ФИО', max_length=255, null=True, blank=True)
    creditals = models.CharField(
        verbose_name='Логин/Пароль ФБ', max_length=255, null=True, blank=True)
    phone = models.CharField(
        verbose_name='Номер телефона', max_length=255, null=True, blank=True)
    login_password = models.CharField(
        verbose_name='Логин/Пароль ПОЧТА', max_length=255, null=True, blank=True)
    profile_url = models.CharField(
        verbose_name='ссылка на профиль', max_length=255, null=True, blank=True)
    dob = models.CharField(
        verbose_name='ДР', max_length=255, null=True, blank=True)
    bm_ur = models.CharField(
        verbose_name='Ссылка на БМ', max_length=255, null=True, blank=True)
    invite_to_bm = models.CharField(
        verbose_name='Пригласить в бм', max_length=255, null=True, blank=True)
    # status_dolphin = models.ForeignKey('app.')

    class Meta:
        verbose_name = 'Фарм Таблица'
        verbose_name_plural = 'Фарм Таблица'

    def __str__(self):
        return self.f_name


for q in DolphinInfo.objects.values('name', 'status'):

    print(q)
