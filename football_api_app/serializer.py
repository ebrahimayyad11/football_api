from rest_framework import serializers

from .models import Football

class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'player_name', 'position', 'created_at', 'manager')
        model = Football