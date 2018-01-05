from rest_framework.serializers import (
ModelSerializer,
ValidationError,
EmailField,
CharField,
)
from comments.models import Comment
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":
        {"write_only": True}
        }
        # why wee need this so after the the user submit their data
        # those data don't appear (password)
    def validate(self, data):
        if len(data['password']) < 8:
            raise ValidationError({"password":
                "This password is too short"})
        email = data['email']
        user_queryset = User.objects.filter(email = email)
        if user_queryset.exists():
            raise ValidationError({"email":
                "A user with that email already exists"})
        return data


    def create(self, validate_data):
        username = validate_data['username']
        email = validate_data['email']
        password = validate_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validate_data

class UserLoginSerializer(ModelSerializer):
    #email = EmailField(label='email')
    username = CharField()
    login = CharField(allow_blank=True, read_only = True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'login',

        ]
        extra_kwargs = {"password":
        {"write_only": True}
        }
        # why wee need this so after the the user submit their data
        # those data don't appear (password)
    def validate(self,data):
        username = data.get("username")
        password = data['password']
        user = User.objects.filter(
        Q(username=username)
        ).distinct()
        if user.exists() and user.count() ==1:
            user_obj = user.first()

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")
        data["login"] ="Successfully"



        return data

class UserUpdateSerializer(ModelSerializer):
    email = EmailField(label='email')
    class Meta:
        model = User
        fields = [
            'email',
            'password',

        ]
        extra_kwargs = {"password":
        {"write_only": True}
        }
        # why wee need this so after the the user submit their data
        # those data don't appear (password)
    def validate(self, data):
        if len(data['password']) < 8:
            raise ValidationError({"password":
                "This password is too short"})
        email = data['email']
        user_id = self.context['request'].user.id
        print (email, user_id)

        user_queryset = User.objects.filter(email = email).exclude(id = user_id)
        if user_queryset.exists():
            raise ValidationError({"user":
                "A user with this email already exists"})
        return data

    def create(self, validate_data):
        #username = validate_data['username']
        email = validate_data['email']
        password = validate_data['password']
        user_obj = User.objects.get(id=self.context['request'].user.id)
        #user_obj.username = username
        user_obj.email = email
        user_obj.set_password(password)
        user_obj.save()
        return validate_data
