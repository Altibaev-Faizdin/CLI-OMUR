from django.urls import path
from rest_framework.routers import DefaultRouter

from app.settings.views import (
    TherapyPageViewSet,
)
router = DefaultRouter()
router.register("main", TherapyPageViewSet, basename="main")

urlpatterns = router.urls
