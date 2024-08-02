from rest_framework import serializers
from .models import User

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()