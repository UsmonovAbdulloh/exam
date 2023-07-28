from rest_framework import serializers
from .models import FieldModel, BookingModel

class FieldModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = '__all__'

class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__'
