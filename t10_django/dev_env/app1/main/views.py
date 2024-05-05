from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context= {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'is_authenticated': False,
        'dict':{
            'first': 'такие дела'
        }
    }
    return render(request, 'main/index.html', context=context)
    # return HttpResponse(' home page ')

def about(request):
    return HttpResponse(' about page ')

