from django.conf.urls import url
from django.contrib import admin

from .views import (
	CommentCreateAPIView,
	CommentListAPIView,
	CommentDetailAPIView,
	CommentUpdateAPIView,
	CommentDeleteAPIView,
	#BlogPostsListAPIView,
	UserCommentListAPIView,
	MyCommentListAPIView,

	)

urlpatterns = [
	url(r'^$', CommentListAPIView.as_view(), name='list'),
	url(r'^me/$', MyCommentListAPIView.as_view(), name='list'),
	#url(r'^blog/$', BlogPostsListAPIView.as_view(), name='blog-posts'),
	url(r'^user/$', UserCommentListAPIView.as_view(), name='user-comments'),
 	url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
	url(r'^(?P<id>[\w-]+)/$', CommentDetailAPIView.as_view(),name = 'detail'),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', CommentUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', CommentDeleteAPIView.as_view(), name= 'delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	# to delete must be POST method

]
