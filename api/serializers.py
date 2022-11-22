from rest_framework import serializers

from content.models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = []
