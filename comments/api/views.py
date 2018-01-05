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
CommentSerializer,
CommentCreateUpdateSerializer,
CommentUserSerializer,
)

from comments.models import Comment
from django.db.models import Q
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CommentCreateUpdateSerializer(data = data, context={"request": request})
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response({"comment":"created"},status=HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

class MyCommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Comment.objects.filter(user = self.request.user)

class UserCommentListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CommentUserSerializer
    def get_queryset(self):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(user__username = query)
            return queryset_list

class CommentUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes= [IsOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    lookup_field = 'id'

class CommentDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes= [IsOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'



class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    #specify which field that we write
    #in the url to get the details
    lookup_url_kwarg = 'id'
    # the argument in the url
    # the defaukt is pk and lookup_field = id by default
