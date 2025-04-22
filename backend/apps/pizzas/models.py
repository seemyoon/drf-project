from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel
from core.services.file_service import upload_pizza_photo

from apps.pizza_shop.models import PizzaShopModel


class DaysChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'


class PizzaModel(BaseModel): # upload_pizza_photo without brackets - you pass a reference to the function, and Django will later call it itself when it saves the image and it will have:
    class Meta:
        db_table = 'pizza'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    photo = models.ImageField(upload_to=upload_pizza_photo, blank=True) # we can use FileField as well, but ImageField has ability to validate picture. blank=True - field can be empty
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')