from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Car


class CarSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'specifications', 'updated', 'time_stamp', 'user', "post"]
        model = Car