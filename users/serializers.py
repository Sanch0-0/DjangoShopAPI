from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from cart.models import Cart


class RegistrationSerializer(serializers.Serializer):

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        password1 = attrs['password1']
        password2 = attrs['password2']

        if password1 != password2:
            raise serializers.ValidationError(
                {"password2": "Passwords did't match"},
                code=400
            )

        return attrs

    def save(self):
        user = User.objects.create(
            email=self.validated_data['email'],
            password=self.validated_data['password1']
        )
        Cart.objects.create(user=user)
        return user


class UpdateSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "full_name",
        ]
