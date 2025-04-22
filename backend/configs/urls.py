from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('api/pizzas', include('apps.pizzas.urls')),
    path('api/pizza_shop', include('apps.pizza_shop.urls')),
    path('api/auth', include('apps.auth.urls')),
    path('api/users', include('apps.user.urls'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# now django understands what we are talking about

# This is needed for working with photos/files (MEDIA) during development (locally), so that Django can serve images (or other media files) by URL.
# This is only needed during development. In production, Nginx or another server should serve media files
# Static - these are static files that do not change on the server and are not linked to the database.