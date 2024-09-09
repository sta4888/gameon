from django.http import HttpResponse
from django.shortcuts import render


def register_view(request):
    return HttpResponse("Hello, world. You're")
