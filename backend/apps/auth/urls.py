from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActivateUserView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    # 'name =' will then be needed for automatic generation of API documentation (Swagger)
    # auth_ - title
    # login - what will do
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate')
]
