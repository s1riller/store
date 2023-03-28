from django.http import HttpResponse
from django.shortcuts import render
from bots.models import Bot
from num2words import num2words
# Create your views here.


def index(request):
    count = Bot.objects.all().count()
    if count == 0:
        title = 'No bots'
    else:
        title = num2words(count, to='ordinal') + ' ' + ('bot' if count == 1 else 'bots' if 2 <= count % 10 <= 4 and (
                    count % 100 < 10 or count % 100 >= 20) else 'bots')
    context = {'title': title,
               'bots': Bot.objects.all()}
    return render(request, 'bots/index.html', context)