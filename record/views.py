from random import random

from django.http import HttpResponse
from django.shortcuts import render

from record.models import Record


# Create your views here.



def index(request):
#   одиночная запись
    record = Record()
    record.title = 'Первая запись'
    record.save()
#   создание нескольких записей
    for i in range(15):
        new_records = Record.objects.create(
            title='новая запись'
        )
    records = Record.objects.all()
    for record in records:
        if str(record.id) not in record.title:
            record.title = f'{record.title} + {record.id}'
        record.save()
    for record in records:
        if int(record.id) % 2 != 0:
            record.delete()
    return HttpResponse('Всё работает!')