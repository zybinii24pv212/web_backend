from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='user')
urlpatterns = router.urls
