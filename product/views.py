from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Product Page')

# Create your views here.
