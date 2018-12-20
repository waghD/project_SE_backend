from rest_framework import serializers
from .models import FreightCompany


class FreightListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location')


class FreightCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = FreightCompany
        fields = ('name', 'location', 'has_own_vehicles', 'rating', 'permissions',
                  'revenue', 'founding_year')
