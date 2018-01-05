from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from posts.models import Post



class Comment(models.Model):
    content     = models.TextField()
    post        = models.ForeignKey(Post)
    #timestamp   = models.DateTimeField(auto_now_add=True, default = timezone.now)
    likes       = models.IntegerField(default = 0)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)




    class Meta:
        ordering = ['-id']


    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)
