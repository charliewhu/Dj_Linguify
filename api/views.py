from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TextSerializer, TextWordSerializer, WordSerializer
from content.models import Text, TextWord, Word


class TextViewSet(viewsets.ModelViewSet):
    serializer_class = TextSerializer
    queryset = Text.objects.all()


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()


class TextWordViewSet(viewsets.ModelViewSet):
    serializer_class = TextWordSerializer

    def get_queryset(self, *args, **kwargs):
        text_id = self.kwargs.get("pk")
        text_words = TextWord.objects.filter(text=text_id)
        return text_words

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
