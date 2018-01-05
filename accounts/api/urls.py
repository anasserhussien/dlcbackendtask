from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserUpdateAPIView,
	)

urlpatterns = [
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^(?P<username>[\w-]+)/change/$', UserUpdateAPIView.as_view(), name='change'),

]
