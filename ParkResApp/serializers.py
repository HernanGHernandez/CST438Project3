from rest_framework import serializers
from ParkResApp.models import User, Messages, LotA, LotB, LotC, LotD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'password')


# class ParkingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parking
#         fields = ('parkingId', 'slot', 'lot', 'parkSwitch', 'userId')


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('messageId', 'message', 'userId', 'parkingId')


class LotASerializer(serializers.ModelSerializer):
    class Meta:
        model = LotA
        fields = '__all__'


class LotBSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotB
        fields = '__all__'


class LotCSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotC
        fields = '__all__'


class LotDSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotD
        fields = '__all__'
