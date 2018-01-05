from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
DestroyAPIView,
UpdateAPIView,
CreateAPIView,
RetrieveDestroyAPIView,
RetrieveUpdateAPIView,
 )

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,
)

from .serializers import (
UserCreateSerializer,
UserLoginSerializer,
UserUpdateSerializer,
)
from .permissions import IsLogged
from comments.models import Comment
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid(raise_exception= True):
            new_data = serializer.data
            u = authenticate(username = data['username'],password = data['password'])
            print (u)
            login(request,u)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

class UserUpdateAPIView(APIView):
    permission_classes = [IsLogged]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field='username'
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserUpdateSerializer(data = data, context={"request": request})
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response({"user":"changes applied"},status=HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


# class UserCommentListAPIView(ListAPIView):
#     permission_classes = [IsAdminUser]
#     serializer_class = CommentUserSerializer
#     def get_queryset(self):
#         queryset_list = Comment.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             queryset_list = queryset_list.filter(Q(user__username__icontains=query))
#             return queryset_list
