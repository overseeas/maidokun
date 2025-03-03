from django import forms

class ItemForm(forms.Form):
    code = forms.CharField(label="自社コード", required=False)
    name = forms.CharField(label="商品名", required=False)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        name = cleaned_data.get('name')
        
        if not code and not name:
            raise forms.ValidationError("どちらかの欄は入力してください。")
        return cleaned_data

class DefaultForm(forms.Form):
    code = forms.CharField(label="自社コード")
    name = forms.CharField(label="商品名")
    product_code = forms.CharField(label="品番")
    jan_code = forms.CharField(label="JANコード")
    list_price = forms.DecimalField(label="定価")
    sales_price = forms.DecimalField(label="実売価格")
    stock_count = forms.DecimalField(label="在庫数")
    bargain_price = forms.DecimalField(label="セール価格")
    model_number = forms.CharField(label="発注型番")
    is_alive = forms.BooleanField(label="廃番")
    is_visible = forms.BooleanField(label="表示中")
