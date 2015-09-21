from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 80)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        db_table = 'products'
        ordering = ['name',]
        
    def __unicode__(self):
        return self.name
        