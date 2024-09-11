from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.template import loader
from django.db.models import F
from django.urls import reverse
from . import apis

from base64 import b64encode
from .models import Item, Sku
from pathlib import Path
import environ
import os
from pytz import timezone
from datetime import datetime

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, 'maidokun/.env'))




def index(request):
    items = Item.objects.all()
    template = loader.get_template("rakuten/index.html")
    
    last_update = Sku.objects.order_by("-updated_at").first().updated_at
    
    context = {
        "items": items,
        "last_update": last_update,
    }
    return HttpResponse(template.render(context, request))

def detail(request, manage_number):
    item = get_object_or_404(Item, manage_number= manage_number)
    skus = get_list_or_404(Sku, item=item.id)

    context = {
        "item": item,
        "skus": skus,
    }
    return render(request, "rakuten/detail.html", context)

def update(request):
    last_update = Sku.objects.order_by("-updated_at").first().updated_at
    items = get_updated_list(last_update)
    for item in items:
        if not(Item.objects.filter(manage_number= item["manageNumber"]).exists()):
            Item.objects.create(manage_number= item["manageNumber"], title=item["title"])
        Item.objects.filter(manage_number= item["manageNumber"]).update(hide_item=item["hideItem"])
        for sku, detail in item["variants"].items():
            if not(Sku.objects.filter(sku_number=sku).exists()):
                Sku.objects.create(sku_number=sku, item= Item.objects.get(manage_number=item["manageNumber"]))
            
            #reference_price
            if "value" in detail["referencePrice"]:
                reference_price = detail["referencePrice"]["value"]
            else:
                reference_price = detail["referencePrice"]["displayType"]

            Sku.objects.filter(sku_number=sku).update(
                standard_price= detail["standardPrice"],
                reference_price= reference_price,
                hidden= detail["hidden"],
            )
    return redirect("rakuten:index")

def get_updated_list(limit_time):
    cursorMark = ""
    next_cursorMark = "*"
    updated_items = []

    while cursorMark != next_cursorMark:
        cursorMark = next_cursorMark
        response = apis.items_search({"hits": "100", "cursorMark": cursorMark})
        for item in response["results"]:
            #"2024-09-11T15:12:48+09:00"
            updated = datetime.strptime(item["item"]["updated"], '%Y-%m-%dT%H:%M:%S%z')
            if updated < limit_time:
                return updated_items
            updated_items.append(item["item"])
        next_cursorMark = response["nextCursorMark"]
    
    return updated_items