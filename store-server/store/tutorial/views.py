from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'tutorial/test.html') #Чтобы использовать заготовку нужно указать место до этой заготовки