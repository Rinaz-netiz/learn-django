from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'marlin'})


def hello(request):
    ok = 'ok'
    return render(request, 'hello.html', {'title': 'Hello, world', 'name': 'John'})
