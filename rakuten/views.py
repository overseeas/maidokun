from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item, Sku

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template("rakuten/index.html")
    context = {
        "item_list": item_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, manage_number):
    return HttpResponse("Rakuten Show page of %s" % manage_number)
