from rest_framework import serializers
from app.settings.models import (
    TherapyPage,
    PopularService,
    TherapyService,
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    PreparationArticleImage,
    FAQ,
    ServiceCategory,
    Service,
    Specialist,
    ClinicLeader,
    AboutClinic,
    AboutClinicImage,
    ClinicHistory,
    ClinicHistoryImage,
    Event,
    EventImage,
    WhyUs,
)


class PatientTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTip
        fields = ("id", "title", "description", "image", "button_text", "button_url")


class VideoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = ("id", "title", "description", "thumbnail", "video_url")


class RecommendedSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedSpecialist
        fields = ("id", "full_name", "specialty", "photo", "profile_url")


class PreparationArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationArticleImage
        fields = ("id", "image", "sort_order")


class PreparationArticleSerializer(serializers.ModelSerializer):
    images = PreparationArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = PreparationArticle
        fields = ("id", "title", "content", "images")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("id", "question", "answer")


class PopularServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularService
        fields = ("id", "title", "short_description", "order")


class TherapyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyService
        fields = ("id", "title", "order")


class TherapyPageSerializer(serializers.ModelSerializer):
    popular_services = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    class Meta:
        model = TherapyPage
        fields = ("id", "title", "description", "banner_image", "popular_services", "services")

    def get_popular_services(self, obj):
        return PopularServiceSerializer(PopularService.objects.all(), many=True).data

    def get_services(self, obj):
        return TherapyServiceSerializer(TherapyService.objects.all(), many=True).data


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "description", "image", "order")


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "slug", "service_type", "services")

    def get_services(self, obj):
        return ServiceSerializer(obj.services.all(), many=True, context=self.context).data


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ("id", "full_name", "specialization", "specialist_type", "experience", "description", "photo", "order")


class ClinicLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicLeader
        fields = ("id", "full_name", "position", "description", "photo")


class AboutClinicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutClinicImage
        fields = ("id", "image", "sort_order")


class AboutClinicSerializer(serializers.ModelSerializer):
    images = AboutClinicImageSerializer(many=True, read_only=True)

    class Meta:
        model = AboutClinic
        fields = ("id", "mission", "values", "images")


class ClinicHistoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicHistoryImage
        fields = ("id", "image", "sort_order")


class ClinicHistorySerializer(serializers.ModelSerializer):
    images = ClinicHistoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = ClinicHistory
        fields = ("id", "title", "description", "order", "images")


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ("id", "image", "sort_order")


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "title", "description", "order", "images")


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ("id", "icon", "title", "description", "order")