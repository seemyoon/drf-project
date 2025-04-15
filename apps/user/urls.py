from django.urls import path

from apps.user.views import UserListCreateView, UserUpdateIsActiveView, UserUpdateIsStaffView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/userUpdateIsActive', UserUpdateIsActiveView.as_view(), name='user_update_is_active'),
    path('/<int:pk>/userUpdateIsStaff', UserUpdateIsStaffView.as_view(), name='user_update_is_staff')
]