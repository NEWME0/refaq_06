from django.contrib import admin
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    ]
