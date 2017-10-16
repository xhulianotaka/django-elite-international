from django.db import models
from django.contrib.auth.models import User

class Testimonial(models.Model):
    author = models.CharField(max_length=250, help_text='(full name of author\'s quote)')
    image = models.ImageField(upload_to='Author_Quotes_Images')
    description = models.CharField(max_length=100, help_text='little author description')
    quote = models.TextField()
    posted_by = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - quote' % (self.author,)
