from django.urls import path

from apps.user.views import (
    BlockUserView,
    SendEmailTestView,
    SendEmailToRecoverPassword,
    UnBlockUserView,
    UserListCreateView,
    UserUpdateIsStaffView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/unblock', UnBlockUserView.as_view(), name='user_unblock'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='user_block'),
    path('/<int:pk>/to_admin', UserUpdateIsStaffView.as_view(), name='user_to_admin'),
    path('/test', SendEmailTestView.as_view(), name='send_email_test'),
    path('/send_email_to_recover_password', SendEmailToRecoverPassword.as_view(), name='send_email_to_recover_password')
    ]