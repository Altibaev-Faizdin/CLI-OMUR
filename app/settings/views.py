from rest_framework import mixins, viewsets
from rest_framework.response import Response

from app.settings.models import TherapyPage
from app.settings.serializers import TherapyPageSerializer


class TherapyPageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TherapyPageSerializer
    queryset = TherapyPage.objects.all()

    def list(self, request, *args, **kwargs):
        page = TherapyPage.objects.first()

        serializer = self.get_serializer(page)

        return Response(serializer.data)