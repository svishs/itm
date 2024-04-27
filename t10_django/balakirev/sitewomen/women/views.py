from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request): # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
    }
    return render(request,'women/index.html', context=data)
    # return HttpResponse("Страница приложения women") # прописываем маршрут для
    # этого в файле урл.пай

def about(request): # HttpRequest -содержит информацию о запросе
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request,'women/about.html', context=data)
    # return HttpResponse("Страница приложения women") # прописываем маршрут для
    # этого в файле урл.пай


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music', ))
        # return HttpResponseRedirect(uri)  # 302
        # return HttpResponsePermanentRedirect(uri) # 301
        return redirect(uri)
        # redirect(index) # редирект через функцию представление
        # redirect('/', permanent=True) # 301 постоянный
        # redirect('/') # 302 временный редирект
        # raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")