from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Получаем данные из валидной формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Аутентифицируем пользователя
            user = auth.authenticate(request, username=username, password=password)
            
            if user is not None:
                # Если пользователь найден и активен
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('main:index'))
                else:
                    form.add_error(None, "Аккаунт отключен")
            else:
                form.add_error(None, "Неверное имя пользователя или пароль")
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))
