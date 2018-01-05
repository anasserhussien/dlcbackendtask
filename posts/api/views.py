from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
DestroyAPIView,
UpdateAPIView,
CreateAPIView,
RetrieveUpdateAPIView,
RetrieveDestroyAPIView,
 )

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,
)

from .serializers import (
PostSerializer,
PostCreateUpdateSerializer,
)
from .permissions import IsOwner
from posts.models import Post
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
class PostCreateAPIView(CreateAPIView):
    permission_classes  =[]
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostCreateUpdateSerializer(data = data, context={"request": request})
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response({"post":"created"},status=HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)



class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

class MyPostListAPIView(ListAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Post.objects.filter(user = self.request.user)
        print(queryset)
        return queryset


class BlogPostsListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(blogs__slug =query)
            return queryset_list

class UserPostsListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(user__username =query)
            return queryset_list

class PostUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'



class PostDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    #specify which field that we write
    #in the url to get the details
    lookup_url_kwarg = 'slug'
    # the argument in the url
    # the defaukt is pk and lookup_field = id by default
