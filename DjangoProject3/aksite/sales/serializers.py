from rest_framework import serializers
from .models import Office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'  # You can specify specific fields here


