from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from posts.models import Post
from blogs.models import blogs
from rest_framework.serializers import (
ModelSerializer,
ValidationError,
)

class PostSerializer(ModelSerializer):
    #users = UserDetailSerializer(read_only= True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'likes',
            'user',
            'blogs',
        ]

class CommentCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            #'id',
            'content',
            'post',
            'user',
        ]
        extra_kwargs = {
            'user': {'read_only': True},

        }

    def validate(self, data):
        user = self.context['request'].user
        post_obj = data['post']
        blog = post_obj.blogs
        data['user'] = user
        b = blogs.objects.filter(id = blog.id).filter(users=user.id)
        if b.count() < 1:
            raise ValidationError({"user":
                "You are not registered for this blog"})
        return data

class CommentSerializer(ModelSerializer):
    class Meta:

        model = Comment
        fields = [
            'id',
            'content',
            'likes',
            'post',
            'user',
        ]

class CommentUserSerializer(ModelSerializer):
    post = PostSerializer(read_only = True)
    class Meta:
        depth=1
        model = Comment
        fields = [
            'id',
            'content',
            'likes',
            'post',
        ]
# take the data and return it in json
