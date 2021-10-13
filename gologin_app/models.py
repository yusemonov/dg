from django.db import models

# Create your models here.
BROWSER_CHOICES = [
    ('chrome', 'chrome')
]


class GoProfiles(models.Model):
    name = models.CharField(
        verbose_name='Имя', max_length=255, null=True, blank=True)
    role = models.CharField(verbose_name='Роль',
                            max_length=255, null=True, blank=True)
    gologing_id = models.CharField(
        verbose_name='Id', max_length=255, null=True, blank=True)
    notes = models.TextField(verbose_name='Заметки',
                             max_length=1000, null=True, blank=True)
    browserType = models.CharField(
        verbose_name='Браузер', max_length=255, choices=BROWSER_CHOICES, null=True, blank=True)
    lockEnabled = models.BooleanField(
        verbose_name='Заблокирован', null=True, blank=True)
    timezone = models.CharField(
        verbose_name='Тайм-Зона', max_length=255, null=True, blank=True)
    navigator = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    geolocation = models.CharField(max_length=255, null=True, blank=True)
    enabled = models.CharField(max_length=255, null=True, blank=True)
    customize = models.CharField(max_length=255, null=True, blank=True)
    fillBasedOnIp = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    accuracy = models.CharField(max_length=255, null=True, blank=True)
    canBeRunning = models.CharField(max_length=255, null=True, blank=True)
    os = models.CharField(max_length=255, null=True, blank=True)
    proxy = models.CharField(max_length=255, null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)
    port = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    autoProxyRegion = models.CharField(max_length=255, null=True, blank=True)
    torProxyRegion = models.CharField(max_length=255, null=True, blank=True)
    proxyType = models.CharField(max_length=255, null=True, blank=True)
    folders = models.CharField(max_length=255, null=True, blank=True)
    sharedEmails = models.CharField(max_length=255, null=True, blank=True)
    shareId = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.CharField(max_length=255, null=True, blank=True)
    updatedAt = models.CharField(max_length=255, null=True, blank=True)
    lastActivity = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профили gologin'
        verbose_name_plural = 'Профили gologin'
