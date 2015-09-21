from django.shortcuts import render
from rest_framework import generics
from cashpoint.models import Product
from cashpoint.serializers import ProductSerializer
# Create your views here.
#List view for Products
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
#get a product
class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer