from django import forms
from .models import Sell

class SellItemForm(forms.ModelForm):

    class Meta:
        model = Sell
        fields = ('title', 'description', 'image', 'choice', 'current_bid', 'buy_it_now', 'time')


# class Submit_Bid(forms.ModelForm):
#     query_results = Sell.objects.all()


class UploadFileForms(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms




