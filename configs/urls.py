from django.urls import include, path

urlpatterns = [
    path('pizzas', include('apps.pizzas.urls')),
    path('pizza_shop', include('apps.pizza_shop.urls')),
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.user.urls'))
]
