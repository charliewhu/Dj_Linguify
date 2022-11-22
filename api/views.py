from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TextSerializer
from content.models import Text

# Create your views here.
class TextViewSet(viewsets.ModelViewSet):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
