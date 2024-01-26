from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME'
    }
    return render(request, 'main/index.html', context)


def about(request):
    pass