from .models import Pictures
from django.shortcuts import render


# Create your views here.
def pictures_upload(request):
    return render(request, "About.html", {'pictures_upload': pictures_upload})