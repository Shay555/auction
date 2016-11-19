"""Auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.contrib.staticfiles import views as static_views
from Hello import views
from blog import urls as blog_urls



urlpatterns = [
    url(r'^home/$', views.get_home, name='home'),
    url(r'^about/$', views.get_index_1, name='about'),
    url(r'^sell/$', views.get_Sell, name='sell'),
    url(r'^buy/$', views.get_Buy, name='buy'),
    url(r'^blog/', include(blog_urls)),
    url(r'^contact/$',views.get_Contact, name='contact'),
    url(r'^privacy/$',views.get_Privacy, name='privacy'),
    url(r'^product/$',views.get_Products, name= 'products' ),
    url(r'^admin/', admin.site.urls),
    #url(r'', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', static_views.serve),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]
