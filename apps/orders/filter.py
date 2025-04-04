
# from django.db.models import QuerySet
# from django.http import QueryDict
# from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from apps.orders.models import DaysChoices, OrderModel

# def filter_order(query: QueryDict) -> QuerySet:
#     queryset = OrderModel.objects.all()
#
#     for k, v in query.items():
#         match k:
#             case 'total_price__gt':
#                 queryset = queryset.filter(total_price__gt=v)
#             case 'total_price__lt':
#                 queryset = queryset.filter(total_price__lt=v)
#             case _:
#                 raise ValidationError({'detail': f'{k} not allowed'})
#     return queryset

class OrdersFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='total_price') # lt, gt as we write these, they will be queryparams
    # field_name='total_price' - field from db
    # lt - the same thing that comes after two __, for instance here: filter(total_price__gt=v)
    range = filters.RangeFilter(field_name='size') # and here we can set min: range_min=2 or max: range_max=100. View:range_min=2&range_max=100
    price_in = filters.BaseInFilter(field_name='price') # This is a filter that checks whether the field (price) contains one of the values passed in the request. If you pass price_in=10,20,30 in the request, then the filter will look for all objects whose price is equal to one of the values 10, 20 or 30.
    # View: /orders/?price_in=10,20,30
    day= filters.ChoiceFilter('day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'id',
            'total_price',
            'status',
        )
    )  # View: asc: order=name, desc: order=-name