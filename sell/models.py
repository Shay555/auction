from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Sell (models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    published_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    current_bid = models.IntegerField(default=0)
    end_date = models.DateTimeField
    #current_high_bid = models.IntegerField


    def publish(self):
        self.published_date = timezone.now()
        self.save()



    # def __unicode__(self):
    #     return self.title

    def __str__(self):
        return self.title


class Bid (models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.ForeignKey(Sell)
    description = models.ForeignKey
    amount = models.IntegerField
    bid_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

