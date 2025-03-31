# In docs, we can see: For example your project's settings.py
# But our rest_conf will extend, so we set settings in the separated file:
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ] # it means for default how it can render, or more precisely json
}
# ability to see json via browser