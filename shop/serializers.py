from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    location = serializers.CharField(max_length=255)
    contact_number = serializers.CharField(max_length=20, required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.save()
        return instance
