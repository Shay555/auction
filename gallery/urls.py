from django.conf.urls import url
import views

urlpatterns = [
    url(r'^gallery/$', views.pictures_upload),
]