from rest_framework import serializers
from .models import book2

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book2
        fields = '__all__'