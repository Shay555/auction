from django.shortcuts import render


# Create your views here.
def get_home(request):
    return render(request, 'Home.html')

def get_index_1(request):
    return render(request, 'About.html')

def get_Sell(request):
    return render(request, 'Sell.html')

def get_Buy(request):
    return render(request,'Buy.html')

#def get_Blog(request):
 #   return render(request, 'blogposts.html' )

def get_Contact(request):
    return render(request, 'Contact-Us.html')

def get_Privacy(request):
    return render(request, 'Privacy-Policy.html')