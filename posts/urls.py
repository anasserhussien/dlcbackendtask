from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
