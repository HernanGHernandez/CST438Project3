from rest_framework import serializers
from ParkResApp.models import User, Parking, Messages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'password')


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('parkingId', 'slot', 'lot', 'parkSwitch', 'userId')


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('messageId', 'message', 'userId', 'parkingId')
