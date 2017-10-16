from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from watson import search as watson
from froala_editor.fields import FroalaField

class Category(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = models.TextField(blank=True, null=True, help_text="(optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = FroalaField()
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='Blog_Images')
    num_views = models.IntegerField(default=0, verbose_name='Views Number')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

watson.register(Post)