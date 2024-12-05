from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    text='sergen'
    context={'text':text}
    return render(request,'index.html',context)

# Create your views here.
