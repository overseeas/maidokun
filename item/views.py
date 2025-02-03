from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm

def index(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item.objects.filter(item_code=form.cleaned_data["item_code"])
            context = {
                    "item" : item
                    }
            return render(request, "item/index.html", {"form": form})
    else:
        form = ItemForm()
    return render(request, "item/index.html", {"form": form})

def create(request):
    if request.method == "POST":
        form = DefaultForm(request.POST)
        if form.is_valid():
            context = {}
            return render(request, "item/index.html", {"form": form})
    else:
        form = DefaultForm()
    return HttpResponseRedirect("item/index.html")
