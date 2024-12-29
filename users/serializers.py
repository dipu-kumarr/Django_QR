from rest_framework import serializers
from .models import User, QRUserLink

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class QRUserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRUserLink
        fields = '__all__'
