from rest_framework import serializers

from content.models import Text, TextWord, Word


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
            "name",
            "status",
        ]


class TextWordSerializer(serializers.ModelSerializer):
    word = serializers.StringRelatedField()
    status = serializers.StringRelatedField(source="get_word_status", read_only=True)

    class Meta:
        model = TextWord
        fields = [
            "id",
            "text",
            "word",
            "status",
        ]
