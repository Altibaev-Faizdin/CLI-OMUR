from rest_framework import mixins, viewsets
from rest_framework.response import Response

from app.settings.models import (
    TherapyPage,
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    PreparationArticleImage,
    FAQ,
    ServiceCategory,
    Service,
    Specialist
)
from app.settings.serializers import (
    TherapyPageSerializer,
    PatientTipSerializer,
    VideoMaterialSerializer,
    RecommendedSpecialistSerializer,
    PreparationArticleSerializer,
    PreparationArticleImageSerializer,
    FAQSerializer,
    ServiceCategorySerializer, 
    ServiceSerializer, 
    SpecialistSerializer
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


class ServiceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SpecialistViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer