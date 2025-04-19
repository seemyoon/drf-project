from django_filters import rest_framework as filters

from apps.pizzas.models import DaysChoices
from apps.pizzas.serializer import PizzaSerializer


class PizzaFilter(filters.FilterSet):
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')

    size_lt = filters.NumberFilter(field_name='size', lookup_expr='lt')
    size_lte = filters.NumberFilter(field_name='size', lookup_expr='lte')
    size_gt = filters.NumberFilter(field_name='size', lookup_expr='gt')
    size_gte = filters.NumberFilter(field_name='size', lookup_expr='gte')

    size_range = filters.RangeFilter(field_name='size')
    price_range = filters.RangeFilter(field_name='price')

    size_in = filters.BaseInFilter(field_name='size')
    price_in = filters.BaseInFilter(field_name='price')

    day = filters.ChoiceFilter(field_name='day', choices=DaysChoices.choices)
    day_istartswith = filters.CharFilter(field_name='day', lookup_expr='istartswith')
    day_iendswith = filters.CharFilter(field_name='day', lookup_expr='iendswith')

    name_lt = filters.CharFilter(field_name='name', lookup_expr='lt')
    name_gt = filters.CharFilter(field_name='name', lookup_expr='gt')
    name_gte = filters.CharFilter(field_name='name', lookup_expr='gte')
    name_lte =filters.CharFilter(field_name='name', lookup_expr='lte')

    order = filters.OrderingFilter(
        fields=PizzaSerializer.Meta.fields
    )
