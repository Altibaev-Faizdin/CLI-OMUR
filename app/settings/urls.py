from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    TherapyPageView,
    CallbackRequestCreateView
)
router = DefaultRouter()
router.register("main", TherapyPageView.as_view(), basename="main")
router.register("callback", CallbackRequestCreateView.as_view(), basename="callback-request")


urlpatterns = router.urls
