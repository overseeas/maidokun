from django import forms
from .models import Margin

class ItemForm(forms.Form):
    item_code = forms.CharField(label="item_code")


class DefaultForm(forms.Form):
    item_code = forms.CharField(label="item_code")
    maker_price = forms.DecimalField(label="maker_price")
    maker_code = forms.CharField(label="maker_code")
    margin_rate = forms.ModelChoiceField(queryset=Margin.objects.all(), empty_label=None)

class RakutenForm(forms.Form):
    manageNumber = forms.CharField(label="manageNumber")

class YahooForm(forms.Form):
    pass

class OchaForm(forms.Form):
    pass

class KakakuComForm(forms.Form):
    pass

class KakakuRobotForm(forms.Form):
    pass
