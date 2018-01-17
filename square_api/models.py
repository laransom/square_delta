# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Result(models.Model):
    number = models.IntegerField(blank=False, null=False)
    solution = models.IntegerField(blank=False, null=False)
    occurences = models.IntegerField(blank=False, null=False)
    
def __str__(self):
    return '%d %d %d' % (self.number, self.solution, self.occurences)