from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save



class blogs(models.Model):
    title = models.CharField(max_length=120, unique = True)
    slug = models.SlugField(unique= True)
    desc = models.TextField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = blogs.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_blog_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_blog_receiver, sender=blogs)
