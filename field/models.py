from django.db import models
from datetime import datetime 


class FieldModel(models.Model):
    name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, default='', blank= True, null=True)
    contact = models.PhoneNumberField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    first_time= models.CharField(max_length=50, blank=True, null=True)
    end_time = models.CharField(max_length=50, blank=True null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_field = 'Field'
