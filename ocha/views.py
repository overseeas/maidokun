from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import OchaStore1Item
from .forms import ItemForm, DefaultForm
import rakuten.models 

def index(request):

    if request.method == "POST":
        try:
            form = ItemForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data["code"]
                name = form.cleaned_data["name"]
                items = []
                if code:
                    items = get_list_or_404(OchaStore1Item, code__contains = code)
                if name:
                    items = get_list_or_404(OchaStore1Item, name__contains = name)
                if items:
                    context = {
                            "form" : form,
                            "items" : items
                            }
                    return render(request, "ocha/index.html", context=context)
                else:
                    messages.warning(request, "検索条件と十分に一致する結果が見つかりません")
        except:
            return render(request, "ocha/index.html", {"form": form})
    else:
        form = ItemForm()
    return render(request, "ocha/index.html", {"form": form})

def create(request):
    if request.method == "POST":
        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            OchaStore1Item.objects.create(
                    code=default_form.cleaned_data["code"],
                    )
            return redirect("/ocha/index")
    else:
        default_form = DefaultForm()


    return render(request, "ocha/create.html", {
        "default_form": default_form,
        })
def detail(request, code):
    context = {
                "code": get_object_or_404(OchaStore1Item, code=code),
            }
    try:
        pass
    except:
        pass

    return render(request, "ocha/detail.html", context=context)
