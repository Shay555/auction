from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sell/$', views.sell_list),
    url(r'^sell/(?P<id>\d+)/$', views.item_detail),
    url(r'^sell/new/$', views.new_post, name='new_post'),

]

