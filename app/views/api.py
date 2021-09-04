from django.http.response import Http404, JsonResponse
from rest_framework import viewsets
from ..serializers import *
from rest_framework.views import APIView
from ..models import *
from rest_framework.permissions import IsAuthenticated

class BugAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BugSerializer
    queryset = Bug.objects.all()