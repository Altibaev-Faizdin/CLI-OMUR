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
)

class PatientTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTip
        fields = ("title", "description", "image", "button_text", "button_url")


class VideoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = ("title", "description", "thumbnail", "video_url")


class RecommendedSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedSpecialist
        fields = ("full_name", "specialty", "photo", "profile_url")


class PreparationArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationArticleImage
        fields = ("image", "sort_order")


class PreparationArticleSerializer(serializers.ModelSerializer):
    images = PreparationArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = PreparationArticle
        fields = ("title", "content", "images")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("question", "answer")



class PopularServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularService
        fields = (
            "title",
            "short_description",
            "order"
        )


class TherapyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyService
        fields = (
            "title",
            "order"
        )


class TherapyPageSerializer(serializers.ModelSerializer):
    popular_services = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    class Meta:
        model = TherapyPage
        fields = (
            "title",
            "description",
            "banner_image",
            "popular_services",
            "services",
        )

    def get_popular_services(self, obj):
        return PopularServiceSerializer(
            PopularService.objects.all(),
            many=True
        ).data

    def get_services(self, obj):
        return TherapyServiceSerializer(
            TherapyService.objects.all(),
            many=True
        ).data


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "description",
            "image",
            "order",
        )


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "slug", "services")

    def get_services(self, obj):
        active = obj.services.filter(is_active=True)
        return ServiceSerializer(active, many=True, context=self.context).data
    

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ("id", "full_name", "specialization", "experience", "photo", "order")
