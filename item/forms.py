from django import forms

class ItemForm(forms.Form):
    item_code = forms.CharField(label="item_code")


class DefaultForm(forms.Form):
    item_code = forms.CharField(label="item_code")
    maker_price = forms.DecimalField(label="maker_price")
    maker_code = forms.CharField(label="maker_code")
    margin_rate = forms.DecimalField(label="margin_rate", max_value=100, min_value=0)
