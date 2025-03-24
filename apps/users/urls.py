from django.urls import path
from apps.users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view()),  # '' is empty, 'cause we specified users in common urls

    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]
