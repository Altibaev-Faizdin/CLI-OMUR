from django.urls import path
from rest_framework.routers import DefaultRouter

from app.settings.views import (
    TherapyPageViewSet,
    PatientTipViewSet,
    VideoMaterialViewSet,
    RecommendedSpecialistViewSet,
    PreparationArticleViewSet,
    FAQViewSet,
    ServiceCategoryViewSet,
    ServiceViewSet,
    SpecialistViewSet,
    ClinicLeaderViewSet,
    AboutClinicViewSet,
    WhyUsViewSet,
    ClinicHistoryViewSet,
    EventViewSet,
)

router = DefaultRouter()
router.register("main", TherapyPageViewSet, basename="main")
router.register("patient-tips", PatientTipViewSet, basename="patient-tips")
router.register("video-materials", VideoMaterialViewSet, basename="video-materials")
router.register("recommended-specialists", RecommendedSpecialistViewSet, basename="recommended-specialists")
router.register("preparation-articles", PreparationArticleViewSet, basename="preparation-articles")
router.register("faqs", FAQViewSet, basename="faqs")
router.register("services", ServiceCategoryViewSet, basename="service-category")
router.register("services-detail", ServiceViewSet, basename="service")
router.register("specialists", SpecialistViewSet, basename="specialist")
router.register("clinic-leader", ClinicLeaderViewSet, basename="clinic-leader")
router.register("about-clinic", AboutClinicViewSet, basename="about-clinic")
router.register("clinic-history", ClinicHistoryViewSet, basename="clinic-history")
router.register("events", EventViewSet, basename="event")
router.register("why-us", WhyUsViewSet, basename="why-us")


urlpatterns = router.urls
