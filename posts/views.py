try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except:
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post




def post_list(request):

	return HttpResponse("<h3>Hello <b>DLC</b> team this is blank page as it's an API app so it means nothing to do UI stuff here </h3>")
