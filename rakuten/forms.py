from django import forms


class SearchFormWithNumber(forms.Form):
    #choice = forms.ChoiceField([("キーワード検索",1), ("複数の管理番号検索",2)])
    #manageNumber = forms.MultiValueField(fields=(forms.CharField(label="キーワード検索"), forms.CharField(label="複数の管理番号検索")), label="検索")
    manageNumber = forms.CharField(label="商品管理番号で検索")
    #manageNumbers = forms.CharField(label="複数の管理番号検索", required=False)

class SearchFormWithTitle(forms.Form):
    
    title = forms.CharField(label="商品名で検索")