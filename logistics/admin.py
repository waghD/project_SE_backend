from django.contrib import admin
from .models import Destination, AirFreightCompany,RailwayFreightCompany,RoadFreightCompany, Truck, Driver, \
    Plane, Train

admin.site.register(Destination)
admin.site.register(AirFreightCompany)
admin.site.register(RailwayFreightCompany)
admin.site.register(RoadFreightCompany)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Plane)
admin.site.register(Train)
