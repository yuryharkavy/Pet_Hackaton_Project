from rest_framework import serializers


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
