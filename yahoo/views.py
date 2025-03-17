from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import YahooMaidoItem, YahooCoordiroomItem
from .forms import ItemForm, DefaultForm
import rakuten.models 
from item.models import Item

import json
import requests
import urllib.parse

def index(request):

    if request.method == "POST":
        try:
            form = ItemForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data["code"]
                name = form.cleaned_data["name"]
                items = []
                if code:
                    item = get_object_or_404(Item, code__contains = code)
                    items = get_list_or_404(YahooMaidoItem, item = item)
                if name:
                    items = get_list_or_404(YahooMaidoItem, name__contains = name)
                if items:
                    context = {
                            "form" : form,
                            "items" : items
                            }
                    return render(request, "yahoo/index.html", context=context)
                else:
                    messages.warning(request, "検索条件と十分に一致する結果が見つかりません")
        except:
            return render(request, "yahoo/index.html", {"form": form})
    else:
        form = ItemForm()
    return render(request, "yahoo/index.html", {"form": form})

def create(request):
    if request.method == "POST":
        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            YahooMaidoItem.objects.create(
                    code=default_form.cleaned_data["code"],
                    )
            return redirect("/yahoo/index")
    else:
        default_form = DefaultForm()


    return render(request, "yahoo/create.html", {
        "default_form": default_form,
        })
def detail(request, code):
    item = get_object_or_404(Item, code=code)
    search_url= "https://shopping.yahoo.co.jp/search?p=" + urllib.parse.quote("ssra56cnt+ダイキン+壁掛形+ペア")
    searched = requests.get(search_url)
    context = {
                "item": item,
                "yahoo": get_object_or_404(YahooMaidoItem, item=item),
                "search_url": search_url,
                "searched": searched,
            }
    try:
        pass
    except:
        pass

    return render(request, "yahoo/detail.html", context=context)
