from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
DestroyAPIView,
UpdateAPIView,
CreateAPIView,
 )

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,

)

from .permissions import IsSuperUser
from .serializers import (
BlogSerializer,
BlogCreateUpdateSerializer,
BlogUserSerializer,
BlogDetailsSerializer,
UserDetailSerializer,
BlogRegisterSerializer,
)

from blogs.models import blogs
from posts.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class BlogUserAPIView(RetrieveAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogUserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'

class BlogCreateAPIView(CreateAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class BlogListAPIView(ListAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUser]


class BlogUpdateAPIView(UpdateAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

class BlogDeleteAPIView(DestroyAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]

class BlogRegisterAPIView(APIView):
    queryset = blogs.objects.all()
    serializer_class = BlogRegisterSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated] # this should be any registered user
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BlogRegisterSerializer(data = data, context={"request": request, "slug":self.kwargs['slug']})
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response({"user":"you are registered now"},status=HTTP_200_OK)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)





class BlogDetailAPIView(RetrieveAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogDetailsSerializer
    lookup_field = 'slug'
    #specify which field that we write
    #in the url to get the details
    lookup_url_kwarg = 'slug'
    # the argument in the url
    # the defaukt is pk and lookup_field = id by default
    permission_classes = [IsAdminUser]
