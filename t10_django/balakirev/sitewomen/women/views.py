from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def index(request): # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
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