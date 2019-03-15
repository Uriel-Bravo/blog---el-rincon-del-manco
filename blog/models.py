from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from blog.utils import unique_slug_generator


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    category = models.ForeignKey('Category', related_name='categories')
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'slug':self.slug})


    def __str__(self):
        return self.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Post)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.name
