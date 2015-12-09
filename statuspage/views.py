from django.shortcuts import render, get_object_or_404
from statuspage.models import *
from django.http import HttpResponse

def index(request):
    context = {
        'services': Service.objects.all(),
        }
    return render(request, 'overview.html', context)

def set_down(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    monitor.status = 'D'
    monitor.save()
    return HttpResponse(status=200, content="Success")

def set_up(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    monitor.status = 'U'
    monitor.save()
    return HttpResponse(status=200, content="Success")
