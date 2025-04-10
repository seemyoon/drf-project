from django.urls import include, path

urlpatterns = [
    path('pizzas', include('apps.pizzas.urls')),
    path('pizza_shop', include('apps.pizza_shop.urls'))
]
