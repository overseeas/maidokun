from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm, DefaultForm
import rakuten.models 

def index(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            items = Item.objects.filter(item_code=form.cleaned_data["item_code"])
            context = {
                    "form" : form,
                    "items" : items
                    }
            return render(request, "item/index.html", context=context)
    else:
        form = ItemForm()
    return render(request, "item/index.html", {"form": form})

def create(request):
    if request.method == "POST":
        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            Item.objects.create(
                    item_code=default_form.cleaned_data["item_code"],
                    maker_price=default_form.cleaned_data["maker_price"],
                    maker_code=default_form.cleaned_data["maker_code"],
                    margin_rate=default_form.cleaned_data["margin_rate"],
                    )
            return redirect("/item/index")
    else:
        default_form = DefaultForm()


    return render(request, "item/create.html", {
        "default_form": default_form,
        })
def detail(request, item_code):
    rakutenitem = get_object_or_404(rakuten.models.Item, manageNumber= "xfx450melle9")
    context = {
        "item_code":item_code,
        "rakuten": rakutenitem
    }
    return render(request, "item/detail.html", context=context)
