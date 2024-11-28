from django import forms


class SearchForm(forms.Form):
    #choice = forms.ChoiceField([("キーワード検索",1), ("複数の管理番号検索",2)])
    #manageNumber = forms.MultiValueField(fields=(forms.CharField(label="キーワード検索"), forms.CharField(label="複数の管理番号検索")), label="検索")
    manageNumber = forms.CharField(label="キーワード検索")
    #manageNumbers = forms.CharField(label="複数の管理番号検索", required=False)