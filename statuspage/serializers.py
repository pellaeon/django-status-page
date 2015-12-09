from rest_framework import serializers
from statuspage.models import *

class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident

class MonitorSerializer(serializers.HyperlinkedModelSerializer):
    #incidents = IncidentSerializer()

    class Meta:
        model = Monitor
        fields = ('pk', 'name', 'status')
