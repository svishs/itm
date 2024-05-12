from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def login(request):
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                # messages.success(request, f"{username}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
            'title':'Home - Авторизация',
            'form': form,

        }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method =='POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
                # messages.success(request, f"{username}, Вы вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title':'Home - Регистрация',
        'form':form,

    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title':'Home - Кабинет',

    }
    return render(request, 'users/profile.html', context)
 

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
    # context = {
    #     'title':'Home - Авторизация',

    # }
    # return render(request, '', context)