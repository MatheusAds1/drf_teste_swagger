from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from aluraflix.views import ProgramaViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix",
      default_version='v1',
      description="Provedor local de séries e filmes",
      terms_of_service="#",
      contact=openapi.Contact(email="contato@api.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated, ),
)

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
