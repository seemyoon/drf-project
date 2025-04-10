from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel


class DaysChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'


class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')