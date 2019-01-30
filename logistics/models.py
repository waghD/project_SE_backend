from django.db import models
from django.db.models import DEFERRED
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class FreightCompany(models.Model):
    def __str__(self):
        return self.name

    @classmethod
    def from_db(cls, db, field_names, values):
        # Default implementation of from_db() (subject to change and could
        # be replaced with super()).
        if len(values) != len(cls._meta.concrete_fields):
            values = list(values)
            values.reverse()
            values = [
                values.pop() if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
            ]
        instance = cls(*values)
        instance._state.adding = False
        instance._state.db = db
        # customization to store the original field values on the instance
        instance._loaded_values = dict(zip(field_names, values))
        return instance

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    location = models.CharField(max_length=100, default='')
    FREIGHT_TYPES = (('AIR', 'Air-Freight'),
                     ('ROAD', 'Road-Freight'),
                     ('RAIL', 'Railway-Freight'),
                     ('SHIP', 'Sea-Freight'),
                     )
    type = models.CharField(choices=FREIGHT_TYPES, default='', max_length=100)
    owner = models.ForeignKey(User, related_name='freightcompany', on_delete=models.SET_NULL, null=True, blank=True)
    has_own_vehicles = models.BooleanField(default=True)
    text = 'To select multiple destinations. Hold CTRL!'
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    destinations = CountryField(multiple=True, blank_label='(select country)', blank=True, help_text=text)
    revenue = models.PositiveIntegerField()
    founding_year = models.DateField(help_text='Date Format=1920-2-10')
    logo = models.ImageField


class ManagerAirFreight(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.type != self._loaded_values['type']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerAirFreight, self).get_queryset().filter(

            type='AIR')


class ManagerRoadFreight(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.type != self._loaded_values['type']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerRoadFreight, self).get_queryset().filter(

            type='ROAD')


class ManagerRailwayFreight(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.type != self._loaded_values['type']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerRailwayFreight, self).get_queryset().filter(

            type='RAIL')


class ManagerSeaFreight(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.type != self._loaded_values['type']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerSeaFreight, self).get_queryset().filter(

            type='SHIP')


class AirFreightCompany(FreightCompany):
    objects = ManagerAirFreight()

    class Meta:
        proxy = True


class RoadFreightCompany(FreightCompany):
    objects = ManagerRoadFreight()

    class Meta:
        proxy = True


class RailwayFreightCompany(FreightCompany):
    objects = ManagerRailwayFreight()

    class Meta:
        proxy = True


class SeaFreightCompany(FreightCompany):
    objects = ManagerSeaFreight()

    class Meta:
        proxy = True


class Vehicle(models.Model):

    def __str__(self):
        return self.name

    @classmethod
    def from_db(cls, db, field_names, values):
        # Default implementation of from_db() (subject to change and could
        # be replaced with super()).
        if len(values) != len(cls._meta.concrete_fields):
            values = list(values)
            values.reverse()
            values = [
                values.pop() if f.attname in field_names else DEFERRED
                for f in cls._meta.concrete_fields
            ]
        instance = cls(*values)
        instance._state.adding = False
        instance._state.db = db
        # customization to store the original field values on the instance
        instance._loaded_values = dict(zip(field_names, values))
        return instance

    VEHICLE_TYPES = (('ROAD', 'Truck'),
                     ('AIR', 'Airplane'),
                     ('RAIL', 'Train'),
                     ('SEA', 'Ship'),
                     )
    types = models.CharField(choices=VEHICLE_TYPES, default='', max_length=100)
    name = models.CharField(default='', max_length=100)
    occupied = models.BooleanField(default=False)
    location = models.CharField(default='', max_length=200)
    donedate = models.DateField(default='1980-02-01')
    builtdate = models.DateField(default='1980-02-01')
    length = models.PositiveSmallIntegerField(null=True)
    maxWeight = models.PositiveIntegerField(default=100)
    owner = models.ForeignKey(User,related_name='vehicles', on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey('Driver', related_name='driver', on_delete=models.SET_NULL, null=True, blank=True)
    goods = models.CharField(max_length=10, blank=True)


class ManagerPlane(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.types != self._loaded_values['types']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerPlane, self).get_queryset().filter(

            types='AIR')

    def create(self, **kwargs):
        kwargs.update({'types': 'AIR'})

        return super(ManagerPlane, self).create(**kwargs)


class ManagerTruck(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.types != self._loaded_values['types']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerTruck, self).get_queryset().filter(

            types='ROAD')

    def create(self, **kwargs):
        kwargs.update({'types': 'ROAD'})

        return super(ManagerTruck, self).create(**kwargs)


class ManagerTrain(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.types != self._loaded_values['types']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerTrain, self).get_queryset().filter(

            types='RAIL')

    def create(self, **kwargs):
        kwargs.update({'types': 'RAIL'})

        return super(ManagerTrain, self).create(**kwargs)


class ManagerShip(models.Manager):

    def save(self, *args, **kwargs):
        if not self._state.adding and (
                self.types != self._loaded_values['types']):
            raise ValueError("Updating type is not allowed")
        super().save(*args, **kwargs)

    def get_queryset(self):
        return super(ManagerShip, self).get_queryset().filter(

            types='Ship')

    def create(self, **kwargs):
        kwargs.update({'types': 'Ship'})

        return super(ManagerShip, self).create(**kwargs)


class Train(Vehicle):
    objects = ManagerTrain()
    company = models.ForeignKey(RailwayFreightCompany, on_delete=models.CASCADE, default='')
    features = models.ManyToManyField('Features', limit_choices_to={'vehicle': 'RAIL'})
    permissions = models.ManyToManyField('Permissions', limit_choices_to={'vehicle': 'RAIL'}, related_name='+')


class Plane(Vehicle):
    objects = ManagerPlane()
    company = models.ForeignKey(AirFreightCompany, on_delete=models.CASCADE, default='')
    features = models.ManyToManyField('Features', limit_choices_to={'vehicle': 'AIR'})
    permissions = models.ManyToManyField('Permissions', limit_choices_to={'vehicle': 'AIR'},related_name='+')


class Ship(Vehicle):
    objects = ManagerShip()
    company = models.ForeignKey(SeaFreightCompany, on_delete=models.CASCADE, default='')
    features = models.ManyToManyField('Features', limit_choices_to={'vehicle': 'SEA'})
    permissions = models.ManyToManyField('Permissions', limit_choices_to={'vehicle': 'SEA'}, related_name='+')


class Truck(Vehicle):
    objects = ManagerTruck()

    licenseplate = models.CharField(max_length=10)
    km_driven = models.PositiveIntegerField()
    permission_until = models.DateField()
    emission_class = models.CharField(max_length=5)
    company = models.ForeignKey(RoadFreightCompany, on_delete=models.CASCADE, default='')
    features = models.ManyToManyField('Features', limit_choices_to={'vehicle': 'ROAD'})
    permissions = models.ManyToManyField('Permissions', limit_choices_to={'vehicle': 'ROAD'}, related_name='+')


class Features(models.Model):
    def __str__(self):
        return self.name

    VEHICLE_TYPES = (('ROAD', 'Truck'),
                     ('AIR', 'Airplane'),
                     ('RAIL', 'Train'),
                     ('SEA', 'Ship'),
                     )
    vehicle = models.CharField(choices=VEHICLE_TYPES, default='', max_length=100)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=100, blank=True)


class Permissions(Features):

    class Meta:
        proxy = True


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
