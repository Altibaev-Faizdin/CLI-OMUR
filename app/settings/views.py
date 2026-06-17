from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from app.settings.enum import ServiceType, SpecialistType
from app.settings.models import (
    TherapyPage,
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    FAQ,
    ServiceCategory,
    Service,
    Specialist,
    ClinicLeader,
    AboutClinic,
    WhyUs,
    ClinicHistory,
    Event,
)
from app.settings.serializers import (
    TherapyPageSerializer,
    PatientTipSerializer,
    VideoMaterialSerializer,
    RecommendedSpecialistSerializer,
    PreparationArticleSerializer,
    FAQSerializer,
    ServiceCategorySerializer,
    ServiceSerializer,
    SpecialistSerializer,
    ClinicLeaderSerializer,
    AboutClinicSerializer,
    WhyUsSerializer,
    ClinicHistorySerializer,
    EventSerializer,
)


class TherapyPageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TherapyPageSerializer
    queryset = TherapyPage.objects.all()

    def list(self, request, *args, **kwargs):
        page = TherapyPage.objects.first()
        serializer = self.get_serializer(page)
        return Response(serializer.data)


class PatientTipViewSet(viewsets.ModelViewSet):
    queryset = PatientTip.objects.all()
    serializer_class = PatientTipSerializer


class VideoMaterialViewSet(viewsets.ModelViewSet):
    queryset = VideoMaterial.objects.all()
    serializer_class = VideoMaterialSerializer


class RecommendedSpecialistViewSet(viewsets.ModelViewSet):
    queryset = RecommendedSpecialist.objects.all()
    serializer_class = RecommendedSpecialistSerializer


class PreparationArticleViewSet(viewsets.ModelViewSet):
    queryset = PreparationArticle.objects.prefetch_related("images")
    serializer_class = PreparationArticleSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ServiceCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all().prefetch_related("services")

    def get_queryset(self):
        queryset = super().get_queryset()
        service_type = self.request.query_params.get("service_type")
        if service_type:
            queryset = queryset.filter(service_type=service_type)
        return queryset

    @action(detail=False, methods=["get"], url_path="types")
    def types(self, request, *args, **kwargs):
        return Response(
            [{"value": value, "label": label} for value, label in ServiceType.choices]
        )


class ServiceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SpecialistViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialist_type = self.request.query_params.get("specialist_type")
        if specialist_type:
            queryset = queryset.filter(specialist_type=specialist_type)
        return queryset

    @action(detail=False, methods=["get"], url_path="types")
    def types(self, request, *args, **kwargs):
        return Response(
            [{"value": value, "label": label} for value, label in SpecialistType.choices]
        )


class ClinicLeaderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ClinicLeader.objects.all()
    serializer_class = ClinicLeaderSerializer


class AboutClinicViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AboutClinic.objects.all().prefetch_related("images")
    serializer_class = AboutClinicSerializer


class ClinicHistoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ClinicHistory.objects.all().prefetch_related("images")
    serializer_class = ClinicHistorySerializer


class EventViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all().prefetch_related("images")
    serializer_class = EventSerializer


class WhyUsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer