from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='user')
urlpatterns = router.urls
