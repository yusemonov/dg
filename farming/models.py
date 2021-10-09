from django.db import models
from django.contrib.auth.models import User


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


# class Farm(models.Model):
#     farmer = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, verbose_name='Фармер')
#     farm_stages = models.ForeignKey(
#         'FarmStages', on_delete=models.CASCADE, null=True, verbose_name='Стадия фарма')
#     accounts_facebook = models.ForeignKey(
#         'AccountsFacebook', on_delete=models.CASCADE, null=True, verbose_name='Аккаунт фб')
