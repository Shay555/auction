from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
# Create your models here.
Choice = (
    ('1', 'Locomotive'),
    ('2', 'Engine'),
    ('3', 'Track'),
    ('4', 'Catalogue'),
    ('4', 'All'),
)

Duration = (
    ('1', '1 weak'),
    ('2', '2 weaks'),
    ('3', '3 weaks'),
)


class Sell (models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    published_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    current_bid = models.IntegerField(default=0)
    buy_it_now = models.IntegerField(default=0)
    end_date = models.DateTimeField
    choice = models.CharField(default=0, max_length=15, choices=Choice)
    time = models.CharField(default=0, max_length=10, choices=Duration)
    remaining = models.IntegerField(default=0)
    #current_high_bid = models.IntegerField



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.buy_it_now,
            "currency": "USD",
            "item_name": self.title,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)


    # def __unicode__(self):
    #     return self.title

    def __str__(self):
        return self.title


# class Bid (models.Model):
#     author = models.ForeignKey('accounts.User')
#     title = models.ForeignKey(Sell)
#     # description = models.ForeignKey(Sell)
#     amount = models.IntegerField
#     bid_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#
#     def __unicode__(self):
#         return self.name

# class Images(models.Model):
#     sell = models.ForeignKey(Sell, default=None)

class Bid (models.Model):
    sell = models.ForeignKey(Sell, related_name="bids")
    amount = models.IntegerField(default=0)