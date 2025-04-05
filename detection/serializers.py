from rest_framework import serializers
from .models import Threat

class ThreatSerializer(serializers.ModelSerializer):
    detected_at_readable = serializers.SerializerMethodField()

    class Meta:
        model = Threat
        fields = ['id', 'threat_type', 'severity', 'details', 'detected_at', 'detected_at_readable']

    def get_detected_at_readable(self, obj):
        return obj.detected_at.strftime("%Y-%m-%d %H:%M:%S")
