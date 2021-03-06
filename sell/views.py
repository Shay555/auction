from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Sell
from .forms import SellItemForm
from .forms import UploadFileForms
from django.shortcuts import render_to_response

# Create your views here.
def sell_list(request):

    sells = Sell.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "Sell.html", {'sell':sells})

def item_detail(request, id):

    sell = get_object_or_404(Sell, pk=id)
    sell.views +=1
    sell.save()
    return render(request, "itemdetail.html", {'sell':sell})

def new_post(request):
    if request.method == "POST":
        form = SellItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(item_detail, post.pk)
    else:
        form = SellItemForm()
    return render(request, 'SellItemForm.html', {'form' : form})


def bid_item(request):
  data = Sell.objects.all()
  return render(request, 'bid.html', {"data": data})










