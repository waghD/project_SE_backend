from rest_framework import serializers
from .models import FreightCompany, Truck, Plane, Train, Driver, Features
from django_countries.serializers import CountryFieldMixin


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Features
        fields = ('name', 'description',)


class FreightListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location')


class PlaneListSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Plane
        fields = ('id', 'name', 'types', 'occupied', 'company','features')


class TrainListSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = ('id','name', 'types', 'occupied','features')


class TruckListSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Truck
        fields = ('id', 'name', 'types', 'occupied', 'features')


class FreightCompanySerializer(CountryFieldMixin, serializers.ModelSerializer):
    logo = serializers.ImageField()

    class Meta:
        model = FreightCompany
        fields = ('name', 'type', 'location', 'rating', 'destinations', 'permissions', 'revenue', 'founding_year', 'logo')  # nopep8


class AirFreightCompanySerializer(FreightCompanySerializer):
    planes = PlaneListSerializer(many=True, read_only=True)

    class Meta(FreightCompanySerializer.Meta):
        fields = FreightCompanySerializer.Meta.fields +('planes',)


class RailwayFreightCompanySerializer(FreightCompanySerializer):
    trains = TrainListSerializer(many=True, read_only=True)

    class Meta(FreightCompanySerializer.Meta):
        fields = FreightCompanySerializer.Meta.fields + ('trains',)


class RoadFreightCompanySerializer(FreightCompanySerializer):
    trucks = TruckListSerializer(many=True, read_only=True)

    class Meta(FreightCompanySerializer.Meta):
        fields = FreightCompanySerializer.Meta.fields + ('trucks',)


class DriverSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Driver
        fields = '__all__'
