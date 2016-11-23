from django import forms
from .models import Sell

class SellItemForm(forms.ModelForm):

    class Meta:
        model = Sell
        fields = ('title', 'description', 'image', 'current_bid')


# class Submit_Bid(forms.ModelForm):
#     query_results = Sell.objects.all()
#


