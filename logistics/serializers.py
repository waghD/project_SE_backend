from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'sender', 'pickup_point', 'dropoff_point', 'pickup_date', 'delivery_date', 'price',
                  'state', 'rating', 'goods'
                  # 'freighter','vehicle', 'driver', For later Implemantation
                  )
