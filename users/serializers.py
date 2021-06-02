from .models import CustomUser
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_superuser(**validated_data)
        print(user.is_superuser)
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'settings')
        extra_kwargs = {
            'password': {'write_only': True}
        }
