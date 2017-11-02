# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class NameStrMixin(object):
    def __str__(self):
        return self.name


class Category(NameStrMixin, models.Model):
    name = models.CharField('Группа товара', max_length=64)


class Product(NameStrMixin, models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа')
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость еденицы, руб.', max_digits=10, decimal_places=2)
