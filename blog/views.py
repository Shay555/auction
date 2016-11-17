from django.shortcuts import render
from django.utils import timezone
from .models import POST


# Create your views here.

def post_list(request):

    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to 'blogposts.html' template
    """

    posts = POST.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})



