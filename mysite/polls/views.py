from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, esse é o meu primeiro site")
# Create your views here.


