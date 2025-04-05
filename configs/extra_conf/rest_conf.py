# In docs, we can see: For example your project's settings.py
# But our rest_conf will extend, so we set settings in the separated file:
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],  # it means for default how it can render, or more precisely json
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # we can choose another optional
    # 'PAGE_SIZE': 2   # we specify quantity of elements on 1 page (from rest_framework)
    # https://www.django-rest-framework.org/api-guide/pagination/#pagination
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagePagination',  # specify custom pagination
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend', # from https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
    ),
}
# ability to see json via browser
