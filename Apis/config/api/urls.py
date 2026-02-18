from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet, ProductoViewSet, producto_list

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'productos', ProductoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('api/productos-manual/', producto_list),
]