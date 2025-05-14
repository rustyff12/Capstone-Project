from rest_framework import serializers
from .models import MenuTable, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = ['id','title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

