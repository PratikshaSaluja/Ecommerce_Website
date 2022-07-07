from rest_framework import serializers
class contactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=1000)
    msg = serializers.CharField(max_length=1000)