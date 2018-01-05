from rest_framework.serializers import (
ModelSerializer,
ValidationError,
CharField,
)
from posts.models import Post
from blogs.models import blogs
from rest_framework.fields import CurrentUserDefault
from blogs.api.serializers import UserDetailSerializer


class PostCreateUpdateSerializer(ModelSerializer):
    #user = CharField(label='user',editable = True)
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'blogs',
            'user',
        ]
        extra_kwargs = {
            'user': {'read_only': True},

        }

    def validate(self, data):
        user = self.context['request'].user
        blog_obj = data['blogs']
        data['user'] = user
        #print(blog_obj.id, user.email)
        b = blogs.objects.filter(id = blog_obj.id).filter(users=user.id)
        if b.count() < 1:
            raise ValidationError({"user":
                "You are not registered for this blog"})
        #print(data)
        return data

class PostSerializer(ModelSerializer):
    #user = UserDetailSerializer(read_only= True)
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'blogs',
            #'publish',
        ]
# take the data and return it in json
