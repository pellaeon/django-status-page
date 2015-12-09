from django.shortcuts import render
from statuspage.models import *
from statuspage.serializers import *
from rest_framework import generics, mixins

def index(request):
    context = {
        'services': Service.objects.all(),
        }
    return render(request, 'overview.html', context)

class MonitorList(generics.ListCreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    #permission_classes = (IsAdminUser,)

class MonitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
