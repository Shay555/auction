# from django.shortcuts import render
from django.shortcuts import render_to_response
# from django.template import RequestContext

def index(request):
    return render_to_response('Home.html')

# Create your views here.
# def get_home(request):
#     return render(request, 'Home.html')

def get_index_1(request):
    return render(request, 'About.html')

def get_Sell(request):
    return render(request, 'Sell.html')

def get_Buy(request):
    return render(request,'Buy.html')

def get_Contact(request):
    return render(request, 'Contact-Us.html')

def get_Privacy(request):
    return render(request, 'Privacy-Policy.html')

# def get_Products(request):
#     return render(request, 'products.html')
