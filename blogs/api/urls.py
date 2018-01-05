from django.conf.urls import url
from django.contrib import admin

from .views import (
	BlogCreateAPIView,
	BlogListAPIView,
	BlogDetailAPIView,
	BlogUpdateAPIView,
	BlogDeleteAPIView,
	BlogUserAPIView,
	BlogRegisterAPIView,
	)

urlpatterns = [
	url(r'^$', BlogListAPIView.as_view(), name='list'),
 	url(r'^create/$', BlogCreateAPIView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', BlogDetailAPIView.as_view(),name = 'detail'),
	url(r'^(?P<slug>[\w-]+)/users/$', BlogUserAPIView.as_view(),name = 'users'),
    url(r'^(?P<slug>[\w-]+)/register/', BlogRegisterAPIView.as_view(),name = 'blog-register'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BlogUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BlogDeleteAPIView.as_view(), name= 'delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	# to delete must be POST method

]
