from rest_framework.serializers import ModelSerializer,Serializer, ValidationError
from blogs.models import blogs
from posts.models import Post
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User
from posts.models import Post

# class UserSerializer(ModelSerializer):
#     username = serializers.CharField()
#     class Meta:
#         model = User
#         exclude = ('password',)

class UserDetailSerializer(ModelSerializer):
    #users = UserDetailSerializer(read_only= True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

class BlogCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = blogs
        fields = [
            #'id',
            'title',
            #'slug',
            'desc',
            'users',
        ]

class BlogRegisterSerializer(ModelSerializer):
    class Meta:
        model = blogs
        fields = [
            #'id',
            #'title',
            #'slug',
            #'desc',
            #'users',
        ]
    def create(self, validate_data):
        #username = validate_data['username']
        blog_slug = self.context['slug']
        user_obj = self.context['request'].user
        blog_obj = blogs.objects.filter(slug = blog_slug)
        if blog_obj:
            blog_obj = blog_obj[0]
            if user_obj not in blog_obj.users.all():
                blog_obj.users.add(user_obj)
                blog_obj.save()
        else:
            raise ValidationError({"blog":
                "this blog doesn't exist"})
        return validate_data


class BlogSerializer(ModelSerializer):
    #users = UserDetailSerializer(read_only= True)
    depth = 1
    class Meta:
        model = blogs
        fields = [
            'id',
            'title',
            'slug',
            'desc',
            'users',
        ]

class BlogUserSerializer(ModelSerializer):
    users = UserDetailSerializer(read_only= True, many= True)
    class Meta:
        model = blogs
        depth = 1
        fields = [
            'users',
        ]

class BlogDetailsSerializer(ModelSerializer):
    users = UserDetailSerializer(read_only= True, many= True)
    class Meta:
        model = blogs
        depth = 1
        fields = [
            'id',
            'title',
            'desc',
            'users',
        ]
# take the data and return it in json
