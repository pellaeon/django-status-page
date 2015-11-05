from django.contrib import admin
from statuspage.models import *

admin.site.register(Incident)
admin.site.register(IncidentChange)
admin.site.register(Monitor)
admin.site.register(Service)
admin.site.register(Host)
