from django.contrib import admin
from cashpoint.models import Product
# Register your models here.
#Admin class for product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_per_page = 50
    ordering = ['name',]
    search_fields = ['name', 'price',]

admin.site.register(Product, ProductAdmin)
    
    