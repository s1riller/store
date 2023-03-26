from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'tutorial/test.html', {
        'title': 'Test Template'})  # Чтобы использовать заготовку нужно указать место до этой заготовки, после передаются данные на форму
