from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from clients.models import Client
from datetime import timedelta
from django.utils import timezone
username_ban_list = ["admin", "маты"]

class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        view = self.context.get("view")
        if view and view.action in ["update", "partial_update"]:
            self.fields["username"].required = False
            self.fields["email"].required = False
            self.fields["password"].required = False

    def validate(self, attrs:dict):
        username = attrs.get("username")
        password = attrs.get("password")
        if username and username in username_ban_list:
            raise serializers.ValidationError("Подобное имя запрещенно")
        if (username and password) and username == password:
            raise serializers.ValidationError("Пароль не может быть таким же как и имя пользователя")

        return super().validate(attrs)
    
    def create(self, validated_data:dict):
        validated_data["password"] = make_password(validated_data["password"])
        validated_data["is_active"] = False
        return super().create(validated_data)
    

    def activate(self, code:str):
        now = timezone.now()
        if not self.is_active and code == self.activation_code and now <= self.code_experetion_date:
            self.is_active = True
            return True
        return False
    
