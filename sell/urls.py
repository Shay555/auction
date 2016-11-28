from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sell/$', views.sell_list),
    url(r'^sell/(?P<id>\d+)/$', views.item_detail),
    url(r'^sell/new/$', views.new_post, name='new_post'),
    url(r'^sell/$', views.bid_item, name='bid'),
    # url(r'^sell/$', views.bid_item, name='bid'),

     # url(r'^sell/bid', views.new_bid),

]

