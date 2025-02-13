from django import forms
from .models import Margin

class ItemForm(forms.Form):
    item_code = forms.CharField(label="item_code")


class DefaultForm(forms.Form):
    item_code = forms.CharField(label="item_code")
    maker_price = forms.DecimalField(label="maker_price")
    maker_code = forms.CharField(label="maker_code")
    margin_rate = forms.ModelChoiceField(queryset=Margin.objects.all(), empty_label=None)
