from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirm']  
        extra_kwargs = {
            'email': {'required': True}
        }

    def validate(self, attrs):
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError('The passwords do not match')
            return attrs

    def create(self, validated_data):
            validated_data.pop('password_confirm')
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user

class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)  # لأنه USERNAME_FIELD = 'email'
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
