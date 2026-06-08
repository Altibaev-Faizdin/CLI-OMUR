from django.urls import path
from rest_framework.routers import DefaultRouter

from app.settings.views import (
    TherapyPageViewSet,
    PatientTipViewSet,
    VideoMaterialViewSet,
    RecommendedSpecialistViewSet,
    PreparationArticleViewSet,
    FAQViewSet
)
router = DefaultRouter()
router.register("main", TherapyPageViewSet, basename="main")
router.register("patient-tips", PatientTipViewSet, basename="patient-tips")
router.register("video-materials", VideoMaterialViewSet, basename="video-materials")
router.register("recommended-specialists", RecommendedSpecialistViewSet, basename="recommended-specialists")
router.register("preparation-articles", PreparationArticleViewSet, basename="preparation-articles")
router.register("faqs", FAQViewSet, basename="faqs")

urlpatterns = router.urls
