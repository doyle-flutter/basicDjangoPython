from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return render(request, 'withexpress/index.html')


def kakaopay(request):
    url = 'http://localhost:3000/expresskakao'
    res = requests.get(url)
    return HttpResponse(content=res)


def err404(request, *args, **argv):
    return render(request, 'withexpress/err404.html', status=404)