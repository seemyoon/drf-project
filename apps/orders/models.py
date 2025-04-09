from django.db import models


class DaysChoices(models.TextChoices):
    monday = 'monday'
    tuesday = 'tuesday'
    wednesday = 'wednesday'
    thursday = 'thursday'
    friday = 'friday'
    saturday = 'saturday'
    sunday = 'sunday'


# Create your models here.
class OrderModel(models.Model):
    class Meta:
        db_table = 'orders'
        ordering = ('-id',) # it will be sort automatically by id

    total_price = models.FloatField()
    quantity_of_products = models.IntegerField()
    status = models.BooleanField()
    comment = models.CharField(max_length=50)
    day = models.CharField(max_length=9,
                           choices=DaysChoices)  # we set choices of smth. and then we need to specify exactly these values (days), not another one
