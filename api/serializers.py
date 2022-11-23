from rest_framework import serializers

from content.models import Text, Word


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = [
            "id",
            "name",
            "body",
        ]


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = [
            "id",
            "status",
        ]
