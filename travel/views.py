from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = 'Aziz'

    return render(request, 'index.html', {'name': name})
