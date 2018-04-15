from .models import Status
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields=('id', 'text', 'created_at')
    def create(self, validated_data):
        return Status.objects.create(**validated_data)