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


@api_view(["GET"])
def text_word(request, pk):
    if request.method == "GET":
        text_word = TextWord.objects.filter(text=pk)
        serializer = TextWordSerializer(text_word, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
