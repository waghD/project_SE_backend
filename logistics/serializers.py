from rest_framework import serializers
from .models import FreightCompany, Truck, Plane, Train, Vehicle, Driver, Features
from django_countries.serializers import CountryFieldMixin
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    freightcompany = serializers.PrimaryKeyRelatedField(many=True, queryset=FreightCompany.objects.all())
    vehicles = serializers.PrimaryKeyRelatedField(many=True,  queryset=Vehicle.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'freightcompany', 'vehicles')


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Features
        fields = ('name', 'description',)


class FreightListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location')


class PlaneListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plane
        fields = ('id', 'name', 'types', 'occupied', 'company')


class TrainListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ('id','name', 'types', 'occupied')


class TruckListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = ('id', 'name', 'types', 'occupied')


class TruckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    driver = serializers.PrimaryKeyRelatedField(many=False, queryset=Driver.objects.all())
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Truck
        fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    driver = serializers.PrimaryKeyRelatedField(many=False, queryset=Driver.objects.all())
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Plane
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    driver = serializers.PrimaryKeyRelatedField(many=False, queryset=Driver.objects.all())
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = '__all__'


class FreightCompanySerializer(CountryFieldMixin,serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FreightCompany
        fields = '__all__'


class AirFreightCompanySerializer(FreightCompanySerializer):
    planes = PlaneListSerializer(many=True, read_only=True)


class RailwayFreightCompanySerializer(FreightCompanySerializer):
    trains = TrainListSerializer(many=True, read_only=True)


class RoadFreightCompanySerializer(FreightCompanySerializer):
    trucks = TruckListSerializer(many=True, read_only=True)


class DriverSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Driver
        fields = '__all__'
