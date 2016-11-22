from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Sell (models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    current_bid = models.IntegerField(default=0)
    end_date = models.DateTimeField
    #current_high_bid = models.IntegerField


    def __str__(self):
        return self.save()

