from django.shortcuts import render, redirect


def index(request):
    """Главная страница."""
    weather = {'temp': '-20',
               'pres': '740'}
    context = {'hello_text': 'Привет, пользователь!',
               'weather': weather}
    return render(request, 'index.html', context)