from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest, StreamingHttpResponse
from django.template import loader
from django.db.models import F
from django.urls import reverse
from .tasks import recently_updated
from .export import *
from .forms import NameForm

from base64 import b64encode
from .models import Item, Sku
from pathlib import Path
import environ
import os
from pytz import timezone
from datetime import datetime, timedelta
import csv

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
    item = get_object_or_404(Item, manageNumber= manage_number)
    skus = get_list_or_404(Sku, item=item.id)

    context = {
        "item": item,
        "skus": skus,
    }
    return render(request, "rakuten/detail.html", context)

def update(request):
    recently_updated.delay()
    return redirect("rakuten:index")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})