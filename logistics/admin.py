from django.contrib import admin
from .models import Region, FreightCompany, Truck, Driver, LiquidTruck, LoadingTruck, \
    ContainerTruck, TemperatureTruck

admin.site.register(Region)
admin.site.register(FreightCompany)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(LiquidTruck)
admin.site.register(LoadingTruck)
admin.site.register(ContainerTruck)
admin.site.register(TemperatureTruck)
