from django.db import models
from core.models import BaseModel

class UserModel(BaseModel): # inherit from BaseModel
    class Meta:  # addition
        db_table = 'users'  # give a name for db

    # id we needn't specify, because it generate automatically with default_auto_field = 'django.db.models.BigAutoField'
    name = models.CharField(max_length=20)  # CharField as varchar, not recommend more than 255
    # specify TextField if you want to specify more than 255
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    weight = models.FloatField()
