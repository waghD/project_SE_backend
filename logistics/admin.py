from django.contrib import admin
from .models import Order, Region, FreightCompany, Vehicle, Truck, Driver, LiquidTruck, LoadingTruck, ContainerTruck, \
    TemperatureTruck

admin.site.register(Order)
admin.site.register(Region)
admin.site.register(FreightCompany)
admin.site.register(Vehicle)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(LiquidTruck)
admin.site.register(LoadingTruck)
admin.site.register(ContainerTruck)
admin.site.register(TemperatureTruck)
