from django.db import models

# Create your models here.
BROWSER_CHOICES = [
    ('chrome', 'chrome')
]


class GoProfiles(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=True)
    role = models.CharField(verbose_name='Роль', max_length=255, null=True)
    gologing_id = models.CharField(
        verbose_name='Id', max_length=255, null=True)
    notes = models.TextField(verbose_name='Заметки',
                             max_length=1000, null=True)
    browserType = models.CharField(
        verbose_name='Браузер', max_length=255, choices=BROWSER_CHOICES, null=True)

    lockEnabled = models.BooleanField(verbose_name='Заблокирован', null=True)
    timezone = models.CharField(
        verbose_name='Тайм-Зона', max_length=255, null=True)
    navigator = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    geolocation = models.CharField(max_length=255, null=True)
    enabled = models.CharField(max_length=255, null=True)
    customize = models.CharField(max_length=255, null=True)
    fillBasedOnIp = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    accuracy = models.CharField(max_length=255, null=True)
    canBeRunning = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True)
    proxy = models.CharField(max_length=255, null=True)
    host = models.CharField(max_length=255, null=True)
    port = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    autoProxyRegion = models.CharField(max_length=255, null=True)
    torProxyRegion = models.CharField(max_length=255, null=True)
    proxyType = models.CharField(max_length=255, null=True)
    folders = models.CharField(max_length=255, null=True)
    sharedEmails = models.CharField(max_length=255, null=True)
    shareId = models.CharField(max_length=255, null=True)
    createdAt = models.CharField(max_length=255, null=True)
    updatedAt = models.CharField(max_length=255, null=True)
    lastActivity = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'Профили gologin'
        verbose_name_plural = 'Профили gologin'
