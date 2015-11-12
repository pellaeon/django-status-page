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

    @property
    def status(self):
        return self.changes.order_by('time')[0].status

    def __str__(self):
        return "%s - %s" % (self.status, self.monitor_set.all()[0].name if self.monitor_set.all() else "")

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

    def __str__(self):
        return "%s - %s" % (self.service_set.all()[0].name if self.service_set.all() else "", self.name)

class Host(models.Model):
    fqdn = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(blank=True, null=True)
    monitors = models.ManyToManyField(Monitor, blank=True)

    def __str__(self):
        return self.fqdn

class Service(models.Model):
    name = models.CharField(max_length=255, default='Unnamed service')
    monitors = models.ManyToManyField(Monitor, blank=True)
    hosts = models.ManyToManyField(Host, blank=True)

    @property
    def status(self):
        for m in self.monitors.all():
            if m.status == Monitor.DOWN:
                return Monitor.DOWN
        for m in self.monitors.all():
            if m.status == Monitor.PARTIAL_DOWN:
                return Monitor.PARTIAL_DOWN
        for m in self.monitors.all():
            if m.status == Monitor.MAINTAINING:
                return Monitor.MAINTAINING
        return Monitor.UP

    def __str__(self):
        return "%s - %s" % (self.name, self.status)