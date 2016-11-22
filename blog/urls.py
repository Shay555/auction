from django.conf.urls import url
#import views
from . import views

urlpatterns =  [
    url(r'^$', views.post_list, name='blog'),
    #url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='blog'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='blog'),

]

