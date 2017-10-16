from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True, help_text='(will be automatically generated)')
    image = models.ImageField(upload_to='Profile_Images')
    description = models.TextField(null=True, blank=True, help_text='(optional)')
    quote = models.TextField(null=True, blank=True, help_text='(optional)')

    def __str__(self):
        return self.user.get_full_name()

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

    try:
        user_full_name = kwargs['instance'].get_full_name()

    except User.DoesNotExist:
        user_full_name = None

    if user_full_name:
        kwargs['instance'].profile.slug = slugify(user_full_name)
        kwargs['instance'].profile.save()

post_save.connect(create_profile, sender=User)