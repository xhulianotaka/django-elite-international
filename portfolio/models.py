from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from watson import search as watson
from froala_editor.fields import FroalaField

class PortfolioCategory(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = models.TextField(blank=True, null=True, help_text="(optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Portfolio_Images')
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = FroalaField()
    category = models.ForeignKey(PortfolioCategory, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    num_views = models.IntegerField(default=0, verbose_name='Views Number')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Portfolio"

watson.register(Portfolio)