from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Pictures(models.Model):
    author = models.ForeignKey('accounts.User')
    image = models.ImageField(upload_to='images', blank=True, null=True)
