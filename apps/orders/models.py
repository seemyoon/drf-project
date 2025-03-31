from django.db import models


# Create your models here.
class OrderModel(models.Model):
    class Meta:
        db_table = 'orders'

    total_price = models.FloatField()
    status = models.BooleanField()
