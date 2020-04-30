# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import JSONField


CHECK_TYPES = (
    ('kitchen', 'Кухня'),
    ('client', 'Клиент'),
)

STATUS = (
    ('new', 'Новый'),
    ('rendered', 'Генерируется'),
    ('printed', 'Напечатан'),
)


class Printer(models.Model):
    name = models.CharField('Имя', max_length=64)
    api_key = models.CharField('API Ключ', max_length=32)
    check_type = models.CharField('Тип чека', choices=CHECK_TYPES, max_length=7)
    point_id = models.IntegerField('Точка')
    
    def __str__(self):
        return f'{self.point_id}: принтер {self.name}'
    
    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
        
        
class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField('Тип чека', choices=CHECK_TYPES, max_length=7)
    order = JSONField('Заказ')
    status = models.CharField('Статус', choices=STATUS, max_length=8)
    pdf_file = models.FileField(upload_to='media/pdf')

    def __str__(self):
        return f'Принтер {self.printer_id}'

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
