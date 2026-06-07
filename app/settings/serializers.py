from rest_framework import serializers
from .models import (
    TherapyPage,
    PopularService,
    TherapyService,
    CallbackRequest
)


class PopularServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularService
        fields = "__all__"


class TherapyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyService
        fields = "__all__"


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

class CallbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackRequest
        fields = ("phone",)
