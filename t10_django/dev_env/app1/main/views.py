from django.http import HttpResponse
from django.shortcuts import render
# подтягиваем модели 
from goods.models import Categories

# Create your views here.

def index(request):

    # categories = Categories.objects.all()
    context= {
        'title': 'Home - Главная',
        'content': 'Магазин часов - HOME',
        # 'categories': categories,

    }
    return render(request, 'main/index.html', context=context)
    # return HttpResponse(' home page ')

def about(request):
    context= {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'что то о магазине'

    }
    return render(request, 'main/about.html', context=context)

