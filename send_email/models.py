from __future__ import unicode_literals

from django.db import models


class UserEmail(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
