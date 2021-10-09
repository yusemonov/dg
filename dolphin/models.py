from django.db import models

class DolphinTags(models.Model):
    tag = models.CharField(verbose_name='Тэги', max_length=255, null=True)

    class Meta:
        verbose_name = 'Тэги'

    def __str__(self):
        return self.tag


class DolphinPermissions(models.Model):
    pass


class DolphinInfo(models.Model):
    dolphin_id = models.IntegerField(verbose_name='ID', null=True, blank=True)
    user_id = models.IntegerField(
        verbose_name='Пользователь', null=True, blank=True)
    group_id = models.CharField(
        verbose_name='ID группы', max_length=255, null=True, blank=True)
    proxy_id = models.IntegerField(
        verbose_name='ID прокси', null=True, blank=True)
    name = models.CharField(
        verbose_name='Имя', max_length=255, null=True, blank=True)
    notes = models.TextField(verbose_name='Заметки',
                             max_length=255, null=True, blank=True)
    tags = models.ManyToManyField('DolphinTags', blank=True)
    permissions = models.ManyToManyField('DolphinPermissions', blank=True)
    user_agent = models.CharField(
        verbose_name='user_agent', max_length=500, null=True, blank=True)
    access_token = models.TextField(
        verbose_name='access_token', max_length=500, null=True, blank=True)
    business_access_token = models.TextField(
        verbose_name='business_access_token', max_length=500, null=True, blank=True)
    fbdtsg = models.TextField(verbose_name='fbdtsg',
                              max_length=500, null=True, blank=True)
    lsd = models.TextField(
        verbose_name='lsd', max_length=255, null=True, blank=True)
    login = models.TextField(verbose_name='login',
                             max_length=255, null=True, blank=True)
    password = models.TextField(
        verbose_name='password', max_length=255, null=True, blank=True)
    cookies = models.TextField(
        verbose_name='cookies', max_length=10000, null=True, blank=True)
    viewport = models.CharField(
        verbose_name='viewport', max_length=255, null=True, blank=True)
    status = models.TextField(verbose_name='status',
                              max_length=255, null=True, blank=True)
    activity_block = models.CharField(
        verbose_name='activity_block', max_length=255, null=True, blank=True)
    archived = models.BooleanField(
        verbose_name='В архиве', null=True, blank=True)
    # error_message = models.Manager()
    fb_id = models.CharField(verbose_name='fb_id',
                             max_length=255, null=True, blank=True)
    fb_name = models.CharField(
        verbose_name='fb name', max_length=255, null=True, blank=True)
    # rules_accepted
    # time_added
    # time_updated
    # time_cabs_updated
    # last_sync
    # proxy
    # bms
    # pages
    # user
    # is_syncing_now


