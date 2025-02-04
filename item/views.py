from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm, DefaultForm, RakutenForm, YahooForm, KakakuComForm, KakakuRobotForm, OchaForm
from rakuten.models import Sku

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
        default_form = DefaultForm(request.POST)
        rakuten_form = RakutenForm(request.POST)
        yahoo_form = YahooForm(request.POST)
        kakaku_com_form = KakakuComForm(request.POST)
        kakaku_robot_form = KakakuRobotForm(request.POST)
        ocha_form = OchaForm(request.POST)

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
        rakuten_form = RakutenForm()
        yahoo_form = YahooForm()
        kakaku_com_form = KakakuComForm()
        kakaku_robot_form = KakakuRobotForm()
        ocha_form = OchaForm()


    return render(request, "item/create.html", {
        "default_form": default_form,
#        "rakuten_form": rakuten_form,
#        "yahoo_form": yahoo_form,
#        "kakaku_com_form": kakaku_com_form,
#        "kakaku_robot_form": kakaku_robot_form,
#        "ocha_form": ocha_form,
        })
