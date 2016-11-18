from django.conf.urls import url
import views

urlpatterns =  [
    url(r'^$', views.post_list, name='blog'),
     url(r'^$', views.post_list, name='blog'),
     url(r'^(?P<id>\d+)/$', views.post_detail, name='blog'),
]

