from django.urls import include, path

urlpatterns = [
    path('users', include('apps.users.urls')),
    path('orders', include('apps.orders.urls'))# specify include to designate path to particular path
]
