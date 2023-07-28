from django.db import models

class FieldModel(models.Model):
    name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Field'


class BookingModel(models.Model):
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.field.name} - {self.start_time} to {self.end_time}"

