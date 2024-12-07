from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/drf-auth/', include('rest_framework.urls')),
                  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/register/', include('authentication.urls')),
                  path('api/products/', include('product.urls')),
                  path('api/cart/', include('cart.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
