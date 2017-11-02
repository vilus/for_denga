# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CustomQuerySet(models.QuerySet):
    def delete(self):
        return self.update(active=False)

    def delete_real(self):
        return super(CustomQuerySet, self).delete()


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class Item(models.Model):
    name = models.CharField('Item', max_length=100)
    active = models.BooleanField('Active', default=True)
    objects = CustomManager()
