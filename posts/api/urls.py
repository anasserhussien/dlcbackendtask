from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostCreateAPIView,
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	BlogPostsListAPIView,
	UserPostsListAPIView,
	MyPostListAPIView,

	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
	url(r'^me/$', MyPostListAPIView.as_view(), name='list'),
	url(r'^blog/$', BlogPostsListAPIView.as_view(), name='blog-posts'),
	url(r'^user/$', UserPostsListAPIView.as_view(), name='user-posts'),
 	url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(),name = 'detail'),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name= 'delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	# to delete must be POST method

]
