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

class Service(models.Model):
    name = models.CharField(max_length=255, default='Unnamed service')

    @property
    def status(self):
        # TODO if service has no monitor -> unknown
        for m in self.monitor_set.all():
            if m.status == Monitor.DOWN:
                return Monitor.DOWN
        for m in self.monitor_set.all():
            if m.status == Monitor.PARTIAL_DOWN:
                return Monitor.PARTIAL_DOWN
        for m in self.monitor_set.all():
            if m.status == Monitor.MAINTAINING:
                return Monitor.MAINTAINING
        return Monitor.UP

    def __unicode__(self):
        return "%s - %s" % (self.name, self.status)

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
    service = models.ForeignKey(Service, blank=True, null=True)
    name = models.CharField(max_length=255, default='Unnamed monitor')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=UP) # manual_status

    def __unicode__(self):
        return "%s - %s" % (self.service_set.all()[0].name if self.service_set.all() else "", self.name)

class Incident(models.Model):
    monitor = models.ForeignKey(Monitor, default=1) #FIXME default=1 might not exist

    @property
    def status(self):
        return self.changes.order_by('time')[0].status

    def __str__(self):
        return "%s - %s" % (self.status, self.monitor.name)

class IncidentChange(models.Model):
    incident = models.ForeignKey(Incident, default=1) #FIXME default=1 might not exist
    status = models.CharField(max_length=1, choices=IncidentBase.INCIDENT_STATUS_CHOICES, default=IncidentBase.DOWN)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, default='')

class Host(models.Model):
    fqdn = models.CharField(max_length=255)
    ip = models.GenericIPAddressField(blank=True, null=True)
    service = models.ForeignKey(Service, default=1) # FIXME default=1 might not exist
    monitors = models.ManyToManyField(Monitor, blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.fqdn, self.ip if self.ip else "")
