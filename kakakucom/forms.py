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
    path = forms.CharField(label="パス")
    name = forms.CharField(label="商品名")
    code = forms.CharField(label="商品コード")
    sub_code = forms.CharField(label="個別商品コード")
    original_price = forms.DecimalField(label="メーカー希望小売価格")
    price = forms.DecimalField(label="通常販売価格")
    sale_price = forms.DecimalField(label="特価")
    options = forms.CharField(label="オプション")
    ship_weight = forms.DecimalField(label="重量")
    display = forms.BooleanField(label="ページ公開")
    delivery = forms.CharField(label="送料無料")
    product_category = forms.CharField(label="プロダクトカテゴリ")
    spec1 = forms.CharField(label="スペック1")
    spec2 = forms.CharField(label="スペック2")
    spec3 = forms.CharField(label="スペック3")
    spec4 = forms.CharField(label="スペック4")
    spec5 = forms.CharField(label="スペック5")