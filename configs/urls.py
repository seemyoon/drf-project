"""
URL configuration for configs project.
"""
from django.urls import path
from myapp.views import MyAppView, MySecondAppView
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('myapp', MyAppView.as_view()),

    # path('mysecondapp/<int:age>', MySecondAppView.as_view()) # we can catch params and sent to MySecondAppView
    path('mysecondapp/<int:age>/<str:name>/<slug:surname>', MySecondAppView.as_view()),
    # slug don't allow set spaces, but can set underscore

    path('users', UserListCreateView.as_view()),

    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]  # list of URL routes.
