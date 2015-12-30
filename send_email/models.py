from __future__ import unicode_literals

from django.db import models


class UserEmail(models.Model):
    email = models.CharField(max_length=200)
