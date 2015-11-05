from django.shortcuts import render
from statuspage.models import *

def index(request):
    context = {
        'services': Service.objects.all(),
        }
    return render(request, 'overview.html', context)

