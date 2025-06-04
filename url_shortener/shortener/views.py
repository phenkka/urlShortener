from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.utils import timezone


class ShortenURLView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        expires = timezone.now() + timezone.timedelta(days=1)
        serializer.save(expires_at=expires)

class ListURLsView(generics.ListAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeactivateURLView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, code):
        try:
            url = ShortURL.objects.get(short_code=code)
            url.is_active = False
            url.save()
            return Response({"message": "Deactivated"}, status=200)
        except ShortURL.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

class RedirectView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, code):
        try:
            url = ShortURL.objects.get(short_code=code, is_active=True)
            if url.is_expired():
                return Response({"error": "Expired"}, status=410)
            url.click_count += 1
            url.save()
            return redirect(url.original_url)
        except ShortURL.DoesNotExist:
            return Response({"error": "Not found"}, status=404)
