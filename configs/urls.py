from django.urls import path, include

urlpatterns = [
    path('users', include('apps.users.urls')),  # specify include to designate path to particular path
]
