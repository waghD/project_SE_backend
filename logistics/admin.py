from django.contrib import admin
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany, Truck, Driver, \
    Plane, Train ,Features, Vehicle, FreightCompany

admin.site.register(AirFreightCompany)
admin.site.register(RailwayFreightCompany)
admin.site.register(RoadFreightCompany)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Plane)
admin.site.register(Train)
admin.site.register(Features)
admin.site.register(Vehicle)
admin.site.register(FreightCompany)
