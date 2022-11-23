from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TextSerializer
from content.models import Text


class TextViewSet(viewsets.ModelViewSet):
    serializer_class = TextSerializer
    queryset = Text.objects.all()


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = TextSerializer
    queryset = Text.objects.all()
