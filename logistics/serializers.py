from rest_framework import serializers
from .models import FreightCompany, Truck,Region


class FreightListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location')


class TruckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('licenseplate','location','occupied','donedate')


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('location','occupied','builtdate', 'donedate','length','licenseplate', 'emptyWeight', 'loadWeight',
                  'km_driven', 'permission_until', 'emission_class')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'country', 'state')


class FreightCompanySerializer(serializers.ModelSerializer):
    vehicles = TruckListSerializer(many=True, read_only=True)
    destinations = RegionSerializer(many=True, read_only=True)

    class Meta:
        model = FreightCompany
        fields = ('name', 'location', 'has_own_vehicles', 'rating', 'permissions',
                  'revenue', 'founding_year', 'vehicles', 'destinations')
