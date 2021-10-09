from django.db import models


class AccountsFacebook(models.Model):
    fb_verbname = models.CharField(
        verbose_name='Человеческое название', max_length=20)
    fb_fname = models.CharField('Имя', max_length=15)
    fb_lname = models.CharField('Фамилия', max_length=15)
    fb_login = models.CharField('Логин', max_length=35)
    fb_pass = models.CharField('Пароль', max_length=35)
    fb_dob = models.DateField('Дата рождения', max_length=20, blank=True)
    fb_eaab = models.TextField('ТОКЕН EAAB', max_length=150, blank=True)
    fb_cookies = models.TextField(
        'Cookies', max_length=5000, blank=True, null=True)
    # fb_fpages = models.ForeignKey('Status', on_delete=models.CASCADE)
    fb_acc_status = models.ForeignKey(
        'Status', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ("%s %s" % (self.fb_verbname, self.fb_login))


class Status(models.Model):
    STATUS_CHOICES = (
        ('BR', 'Бан/Удален'),
        ('CHECK', 'Чек'),
        ('BN', 'Бан, но льется'),
        ('BD', 'Бан, нужны новые доки и разбанить'),
        ('NL', 'Не личность, но льётся'),
    )


class Cookies(models.Model):
    cookies = models.TextField(
        verbose_name='Комментарии к файлу', max_length=5000, blank=True, null=True)
    filescookie = models.FileField(upload_to='cookies/', blank=True)

    class Meta:
        verbose_name_plural = 'Кукки'

    def __str__(self):
        return self.cookies
