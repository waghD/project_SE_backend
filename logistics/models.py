from django.db import models

"""""class Order(models.Model):

    def __str__(self):
        return self.id.__str__()
    id = models.AutoField(primary_key=True)
    freighter = models.ForeignKey('FreightCompany', blank=True, on_delete=models.CASCADE, null=True)
    sender = models.CharField(max_length=150)
    pickup_point = models.TextField(default=' ')
    dropoff_point = models.TextField(default=' ')
    pickup_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    price = models.PositiveIntegerField()
    vehicle = models.ForeignKey('Vehicle', blank=True, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey('Driver', blank=True, on_delete=models.SET_NULL, null=True)
    state = models.BooleanField(default=False)
<<<<<<< HEAD
    rating = models.PositiveSmallIntegerField(blank=True)
    goods = models.TextField(default=' ')"""
=======
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    goods = models.TextField(default=' ')
>>>>>>> c957368e5c6ffeb3ed410d60c4950247d133a8c6


class Region(models.Model):
    def __str__(self):
        return self.name
    name = models.TextField(primary_key=True)
    country = models.TextField()
    state = models.TextField()


class FreightCompany(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    location = models.TextField()
    has_own_vehicles = models.BooleanField(default=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    permissions = models.TextField()
    revenue = models.PositiveIntegerField()
    founding_year = models.DateField()
    destinations = models.ManyToManyField(Region, through='Destination', through_fields=('freighter', 'region'))
    logo = models.Empty


class Destination(models.Model):
    freighter = models.ForeignKey(FreightCompany, on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)


class Vehicle(models.Model):
    company = models.ForeignKey(FreightCompany, on_delete=models.CASCADE, default='')
    occupied = models.BooleanField(default=False)
    location = models.TextField(null=True)
    donedate = models.DateField(default='1980-02-01')
    builtdate = models.DateField(default='1980-02-01')
    length = models.PositiveSmallIntegerField(null=True)

    class Meta:
        abstract = True


class Truck(Vehicle):
    def __str__(self):
        return 'Vehicle ' + str(self.pk)
    licenseplate = models.CharField(max_length=10)
    emptyWeight = models.PositiveIntegerField()
    loadWeight = models.PositiveIntegerField()
    km_driven = models.PositiveIntegerField()
    permission_until = models.DateField()
    emission_class = models.CharField(max_length=5)


class CraneTruck(Truck):
    crane_class = models.TextField()
    wind = models.BooleanField()
    range = models.PositiveIntegerField()


class ContainerTruck(Truck):
    container_length = models.PositiveIntegerField()
    container_width = models.PositiveIntegerField()
    container_height = models.PositiveIntegerField()
    has_ramp = models.BooleanField()


class TemperatureTruck(Truck):
    cooling_power = models.PositiveIntegerField()


class LiquidTruck(Truck):
    liquids = models.CharField(max_length=150)
    liters = models.PositiveIntegerField()
    dangerous_goods = models.BooleanField()
    point_of_entry = models.CharField(max_length=100)


class LoadingTruck(Truck):
    has_walls = models.BooleanField()
    has_sticks = models.BooleanField()


class Driver(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(FreightCompany, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=200)
    gebd_dat = models.DateField()
    rating = models.PositiveSmallIntegerField()
    driving_license_classes = models.CharField(max_length=250)
    work_experience = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)

