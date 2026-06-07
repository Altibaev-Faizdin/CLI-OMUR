from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    TherapyPage,
    CallbackRequest
)

from .serializers import (
    TherapyPageSerializer,
    CallbackRequestSerializer
)


class TherapyPageView(APIView):
    def get(self, request):
        page = TherapyPage.objects.first()

        serializer = TherapyPageSerializer(page)

        return Response(serializer.data)


class CallbackRequestCreateView(generics.CreateAPIView):
    queryset = CallbackRequest.objects.all()
    serializer_class = CallbackRequestSerializer
