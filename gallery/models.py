from django.db import models
from django.contrib.auth.models import User

class ImageGallery(models.Model):
    image = models.ImageField(upload_to='Gallery_Images')
    description = models.TextField(help_text='(optional)', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Image Gallery'

    def __str__(self):
        return '%s - image' % (self.description,)