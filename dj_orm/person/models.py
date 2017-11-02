# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField('person', max_length=100)
    birthday = models.DateField(null=False, blank=False)
