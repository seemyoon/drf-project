REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        # take from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly in pizza app we set it
    ],  # IsAdminUser is the higher permission. then we chan on super-admin
    # and even we didn't set 'permission class' in pizza - for default admin have permission to move this endpoint (getPizza for instance)
    'EXCEPTION_HANDLER': 'core.handlers.error_handler.error_handler' # 1 error_handler is file and 2 is function

}
