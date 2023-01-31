from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):

    # Class that describes how the outer class should work
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'created_at')
        model = Car


