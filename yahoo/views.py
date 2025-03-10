from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import YahooMaidoItem, YahooCoordiroomItem
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
                    items = get_list_or_404(YahooMaidoItem, code__contains = code)
                if name:
                    items = get_list_or_404(YahooMaidoItem, name__contains = name)
                if items:
                    context = {
                            "form" : form,
                            "items" : items
                            }
                    return render(request, "yahoo/index.html", context=context)
                else:
                    messages.warning(request, "検索条件と十分に一致する結果が見つかりません")
        except:
            return render(request, "yahoo/index.html", {"form": form})
    else:
        form = ItemForm()
    return render(request, "yahoo/index.html", {"form": form})

def create(request):
    if request.method == "POST":
        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            YahooMaidoItem.objects.create(
                    code=default_form.cleaned_data["code"],
                    )
            return redirect("/yahoo/index")
    else:
        default_form = DefaultForm()


    return render(request, "yahoo/create.html", {
        "default_form": default_form,
        })
def detail(request, code):
    context = {
                "code": get_object_or_404(YahooMaidoItem, code=code),
            }
    try:
        pass
    except:
        pass

    return render(request, "yahoo/detail.html", context=context)
