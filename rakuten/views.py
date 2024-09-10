from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, request
from django.template import loader
from django.db.models import F
from django.urls import reverse


from .models import Item, Sku
from pathlib import Path
import environ
import os

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, 'maidokun/.env'))

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template("rakuten/index.html")
    context = {
        "item_list": item_list,
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
    
    return redirect(to="rakuten:index")