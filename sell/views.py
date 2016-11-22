from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Sell

# Create your views here.
def sell_list(request):

    sell = Sell.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "Sell.html", {'sell':sell})

def item_detail(request, id):

    sell = get_object_or_404(Sell, pk=id)
    sell.views +=1
    sell.save()
    return render(request, "itemdetail.html", {'sell':sell})