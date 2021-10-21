from rest_framework import serializers
from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Currency
        fields = ('id', 'name', 'rate')

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.id('email', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance