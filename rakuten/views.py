from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import F
from django.urls import reverse

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
    item = Item.objects.get(manage_number = manage_number)
    skus = get_list_or_404(Sku, item=item.id)

    context = {
        "item": item,
        "skus": skus,
    }
    return render(request, "rakuten/detail.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
