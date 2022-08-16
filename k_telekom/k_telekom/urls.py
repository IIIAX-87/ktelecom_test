from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from equipment import views

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet, basename='Equipment')
router.register(r'equipment-type', views.EquipmentTypeViewSet, basename='EquipmentType')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]