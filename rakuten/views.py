from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest, StreamingHttpResponse
from django.template import loader
from django.db.models import F
from django.urls import reverse
from .tasks import update_all
from .export import *
from .forms import SearchForm

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



def detail(request, manage_number):
    item = get_object_or_404(Item, manageNumber= manage_number)
    skus = get_list_or_404(Sku, item=item.id)

    context = {
        "item": item,
        "skus": skus,
    }
    return render(request, "rakuten/detail.html", context)


def update(request):
    update_all()
    return redirect("rakuten:search")

def search(request):
    count = Item.objects.count()
    last_update = Sku.objects.order_by("-updated_at").first().updated_at

    # if this is a POST request we need to process the form data
    if request.method == "GET":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        if form.is_bound:
            # check whether it's valid:
            if form.is_valid():
                manageNumber = form.cleaned_data["manageNumber"]

                items = get_list_or_404(Item, manageNumber__contains = manageNumber)
                context = {
                    "form": form,
                    "items": items,
                    "count": count,
                    "last_update": last_update,
                }
                return render(request, "rakuten/search.html", context)
    form = SearchForm()
    context = {
        "form": form,
        "count": count,
        "last_update": last_update,
    }

    return render(request, "rakuten/search.html", context)