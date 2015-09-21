from rest_framework import serializers
from cashpoint.models import Product

#create serializer class for Product Model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price',)