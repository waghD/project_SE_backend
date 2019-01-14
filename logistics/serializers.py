from rest_framework import serializers
from .models import FreightCompany, Truck, Plane, Train, Destination, Vehicle


class FreightListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location')


class PlaneListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plane
        fields = ('name', 'types', 'occupied')


class TrainListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ('name', 'types', 'occupied')


class TruckListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = ('name', 'types', 'occupied')


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('name', 'country', 'state')


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class FreightCompanySerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True)

    class Meta:
        model = FreightCompany
        fields = '__all__'

    def create(self, validated_data):
        destinations_data = validated_data.pop['destinations']
        freightcompany = FreightCompany.objects.create(**validated_data)
        for destination_data in destinations_data:
            Destination.objects.create(**destination_data)
        return freightcompany


class AirFreightCompanySerializer(FreightCompanySerializer):
    planes = PlaneListSerializer(many=True, read_only=True)


class RailwayFreightCompanySerializer(FreightCompanySerializer):
    trains = TrainListSerializer(many=True, read_only=True)


class RoadFreightCompanySerializer(FreightCompanySerializer):
    trucks = TruckListSerializer(many=True, read_only=True)

