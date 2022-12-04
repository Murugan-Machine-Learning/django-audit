from rest_framework import serializers

from api.models import UdyamForm


class UdyamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UdyamForm
        exclude = ['id', 'created_at', 'updated_at', 'status']
