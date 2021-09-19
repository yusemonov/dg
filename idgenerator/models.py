
from __future__ import unicode_literals
from django.db import models
CHOICE_DATE = [
    ('JAN', 'СІЧ/JAN'),
    ('JUL', 'ЛИП/JUL'),
    ('FEB', 'ЛЮТ/FEB'),
    ('AUG', 'СЕР/AUG'),
    ('MAR', 'БЕР/MAR'),
    ('SEP', 'ВЕР/SEP'),
    ('APR', 'КВІ/APR'),
    ('OCT', 'ЖОВ/OCT'),
    ('MAY', 'ТРА/MAY'),
    ('NOV', 'ЛИС/NOV'),
    ('JUN', 'ЧЕР/JUN'),
    ('DEC', 'ГРУ/DEC'),
]

GENDER_CHOICE = [
    ('M', 'M'),
    ('F', 'F')
]


class Doc(models.Model):
    typedoc = models.CharField(
        verbose_name='Тип/Туре', default='P', max_length=2)
    country = models.CharField(
        verbose_name='Код Страны/Соde of stаte', default='UKR', max_length=3)
    surname = models.CharField(
        verbose_name='Фамилия/Surname', default='ТКАЧЕНКО', max_length=32)
    given_name = models.CharField(
        verbose_name='Имя/name', default="МАР'ЯНА", max_length=32)
    passport_number = models.CharField(
        verbose_name='Номер паспорта', default='PO894599', max_length=8)
    genre = models.CharField(
        verbose_name='Пол', choices=GENDER_CHOICE, default='F', max_length=4)
    nationality = models.CharField(
        verbose_name='Национальность', default='UKRAINE', max_length=32)
    birth_date = models.CharField(
        verbose_name='Дата рождения YYMMDD', default='22', max_length=10)
    personal_number = models.CharField(
        verbose_name='Персональний N/ Personal No.', default='EH № 13251', max_length=10)
    locations = models.CharField(
        verbose_name='Место рождения', default='Київ/UKR', max_length=26)
    id_number = models.CharField(
        verbose_name='Номер паспорта', default='1234567890', max_length=10)
    data_start = models.CharField(
        verbose_name='Дата выдачи/Date of issue YYMMDD', default='190719', max_length=13)
    exp_date = models.CharField(
        verbose_name='Дата окончания YYMMDD', default='290722', max_length=8)
    issuing = models.CharField(
        verbose_name='Орган Выдачи YYMMDD', default='9099', max_length=20)
    photo_doc = models.ImageField(upload_to='cfg/input/')

    class Meta:
        verbose_name = 'Пасспорт'
        verbose_name_plural = 'Пасспорт'
