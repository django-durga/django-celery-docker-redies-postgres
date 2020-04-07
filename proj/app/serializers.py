from .models import Customer
from rest_framework import serializers
from django.contrib.auth.models import User


class Customerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'created', 'name', 'address', 'email',]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_staff=serializers.BooleanField(default=False)
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],is_staff=validated_data['is_staff'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password",'is_staff' )


class MailSerializer(serializers.Serializer):
   email_id = serializers.CharField()
   email_content = serializers.CharField()