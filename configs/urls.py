"""
URL configuration for configs project.
"""
from django.urls import path
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users', UserListCreateView.as_view()),

    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]  # list of URL routes.
