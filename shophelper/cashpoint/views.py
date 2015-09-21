from django.shortcuts import render_to_response
from rest_framework import generics
from cashpoint.models import Product
from cashpoint.serializers import ProductSerializer
# Create your views here.
#driver view 
def index(request):
    return render_to_response('cashpoint/index.html',{})

#List view for Products
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
#get a product
class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer