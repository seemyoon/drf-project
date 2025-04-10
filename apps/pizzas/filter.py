
from django_filters import rest_framework as filters

from apps.pizzas.models import DaysChoices


class PizzaFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    range = filters.RangeFilter(field_name='size')
    price_in = filters.BaseInFilter(field_name='price')
    day = filters.ChoiceFilter(field_name='day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'id',
            'name',
            'price'
        )
    )