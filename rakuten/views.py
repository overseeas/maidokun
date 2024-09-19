from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.template import loader
from django.db.models import F
from django.urls import reverse
from .tasks import recently_updated

from base64 import b64encode
from .models import Item, Sku
from pathlib import Path
import environ
import os
from pytz import timezone
from datetime import datetime, timedelta

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, 'maidokun/.env'))




def index(request):
    items = Item.objects.all()[:10]
    count = Item.objects.count()
    template = loader.get_template("rakuten/index.html")
    
    last_update = Sku.objects.order_by("-updated_at").first().updated_at


    context = {
        "items": items,
        "last_update": last_update,
        "count": count,
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
    test_date = datetime.strptime("2024-09-19T15:00:41+09:00", '%Y-%m-%dT%H:%M:%S%z')
    recently_updated.delay(last_update)
    return redirect("rakuten:index")