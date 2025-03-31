from django.urls import path

from apps.orders.views import OrdersAddOrdersView, OrdersListCreateView

urlpatterns = [
    path('', OrdersListCreateView.as_view()),
    path('/<int:pk>/users', OrdersAddOrdersView.as_view())
]
