from django import forms

class ItemForm(forms.Form):
    code = forms.CharField(label="商品コード", required=False)
    name = forms.CharField(label="商品名", required=False)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        name = cleaned_data.get('name')
        
        if not code and not name:
            raise forms.ValidationError("どちらかの欄は入力してください。")
        return cleaned_data

class DefaultForm(forms.Form):
    code = forms.CharField(label="商品コード")