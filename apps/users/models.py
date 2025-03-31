from django.db import models

from core.models import BaseModel

from apps.orders.models import OrderModel


class UserModel(BaseModel): # inherit from BaseModel
    class Meta:  # addition
        db_table = 'users'  # give a name for db

    # id we needn't specify, because it generate automatically with default_auto_field = 'django.db.models.BigAutoField'
    name = models.CharField(max_length=20)  # CharField as varchar, not recommend more than 255
    # specify TextField if you want to specify more than 255
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    weight = models.FloatField()
    orders =models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='users')
    # ForeignKey - This means that the current model will have a many-to-one relationship with OrderModel.
    # related_name='users' - This means that OrderModel will have a .users attribute that will allow you to get all the users associated with this order.
    # CASCADE - fully deleting
    # Protect - when we deleted user, we can not delete order
    # Set_null - when we deleted, there will be null in all cells. And add null=true as well
    # Default - there will be value, which we need to specify as default after deleted. And add default=... as well
