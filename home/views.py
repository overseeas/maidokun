from django.shortcuts import render
from django.template import loader

# Create your views here.
def top(request):
    context = {}
    return render(request, "home/top.html", context)