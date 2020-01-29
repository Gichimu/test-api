from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name','description','price')
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('items','quantity')