from django.shortcuts import render
from .serializer import *
# Create your views here.
class ItemList(APIView):
    def get(self,request,format=None):
        all_items = Item.objects.all()
        serializers = ItemSerializer (all_items,many=True)
        return Response(serializers.data)

class OrderSerializer(APIView):
    def get(self,request,format=None):
        all_orders = Order.objects.all()
        serializers = OrderSerializer(all_orders,many=True)
        return Response(serializers.data)