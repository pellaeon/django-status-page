from django.shortcuts import render
from statuspage.models import *
from statuspage.serializers import *
from rest_framework import generics, mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

def index(request):
    context = {
        'services': Service.objects.all(),
        }
    return render(request, 'overview.html', context)

@permission_classes((IsAdminUser, ))
class MonitorList(generics.ListCreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    #permission_classes = (IsAdminUser,)

@permission_classes((IsAdminUser, ))
class MonitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
