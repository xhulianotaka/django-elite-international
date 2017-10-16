from django.db import models
from django.contrib.auth.models import User
from watson import search as watson

class BoardMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=250, help_text='(member position in the company)')
    image = models.ImageField(upload_to='Member_ProfileImages')
    slug = models.SlugField(unique=True, help_text=('(will be automatically generated)'), blank=True, null=True)
    description = models.TextField(help_text='(member biography)')
    quote = models.TextField(help_text='(member quote, optional)', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name,)

    def get_member_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

    class Meta:
        ordering = ['-created_at']

watson.register(BoardMember)

class SkillsMember(models.Model):
    skill = models.CharField(max_length=200)
    evaluation = models.IntegerField(help_text='put an integer number between 0 and 100')
    member = models.ForeignKey(BoardMember, related_name='abilities')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Skills Member'

    def __str__(self):
        return self.skill
