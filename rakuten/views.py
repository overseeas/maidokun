from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rakutens = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developer'},
]

def home(request):
    context = {'rakutens': rakutens}
    return render(request, 'rakuten/home.html', context)

def rakuten(request, pk):
    rakuten = None

    for i in rakutens:
        if i['id'] == int(pk):
            rakuten = i
    context = {'rakuten': rakuten}
    return render(request, 'rakuten/rakuten.html', context)
