from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='API Documentation',
        default_version='v1',
        description='API for dds project',
        terms_of_service='Not now',
        contact=openapi.Contact(email='email@email.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
)

urlpatterns = [
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Admin
    path('admin/', admin.site.urls),
    # Welcome
    path('', include('vocabulare.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)