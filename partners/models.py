from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):
    name = models.CharField(max_length=250, help_text='(company name)')
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = models.TextField(help_text='(company description, optional)', blank=True, null=True)
    image = models.ImageField(upload_to='Partners_Images')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s partner' % self.name