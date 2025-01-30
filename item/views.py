from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemCodeForm

def index(request):

    if request.method == "POST":
        form = ItemCodeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = ItemCodeForm()
    return render(request, "item/index.html", {"form": form})
