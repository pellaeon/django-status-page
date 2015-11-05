from django.db import models
from django.utils import timezone

class IncidentBase(object):
    DOWN = 'D'
    INVESTIGATING = 'V'
    IDENTIFIED = 'I'
    WATCHING = 'W'
    FIXED = 'F'

    INCIDENT_STATUS_CHOICES = (
            (DOWN, 'Down'),
            (INVESTIGATING, 'Investigating'),
            (IDENTIFIED, 'Identified'),
            (WATCHING, 'Watching'),
            (FIXED, 'Fixed'),
            )

class IncidentChange(models.Model):
    status = models.CharField(max_length=1, choices=IncidentBase.INCIDENT_STATUS_CHOICES, default=IncidentBase.DOWN)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, default='')

class Incident(models.Model):
    changes = models.ManyToManyField(IncidentChange)

class Monitor(models.Model):
    DOWN = 'D'
    UP = 'U'
    PARTIAL_DOWN = 'P'
    MAINTAINING = 'M'
    
    STATUS_CHOICES = (
            (DOWN, 'Down'),
            (UP, 'Up'),
            (PARTIAL_DOWN, 'Partial down'),
            (MAINTAINING, 'Maintaining'),
            )
    name = models.CharField(max_length=255, default='Unnamed monitor')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=UP)
    incidents = models.ManyToManyField(Incident, blank=True)

class Host(models.Model):
    fqdn = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(blank=True, null=True)
    monitors = models.ManyToManyField(Monitor, blank=True)

class Service(models.Model):
    name = models.CharField(max_length=255, default='Unnamed service')
    monitors = models.ManyToManyField(Monitor, blank=True)
    hosts = models.ManyToManyField(Host, blank=True)
