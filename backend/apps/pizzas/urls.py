from django.urls import path

from apps.pizzas.views import PizzaAddPhoto, PizzaListCreateView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaListCreateView.as_view()),
    path('/<int:pk>', PizzaRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photos', PizzaAddPhoto.as_view())
]
