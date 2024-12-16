from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Um site sobre saúde mental do homem está sendo criado")