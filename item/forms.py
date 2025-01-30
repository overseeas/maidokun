from django import forms

class ItemCodeForm(forms.Form):
    iten_code = forms.CharField(label="自社コード")

