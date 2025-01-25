from django.urls import path,include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
# from .views import




router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)



urlpatterns = [
    # path('auth/', include('auth_app.urls')),
    # path('',include(router.urls)),

    # Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   
]