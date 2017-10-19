from django.db import models
from django.contrib.auth.models import User
from watson import search as watson
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from taggit.models import *
from froala_editor.fields import FroalaField

class JobCategory(models.Model):
    name = models.CharField(max_length=260)
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = FroalaField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

TYPE = (
        ('P', 'Permanent'),
        ('C', 'Contract'),
        ('I', 'Internship'),
    )

class Job(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(unique=True, help_text='(will be automatically generated)')
    description = FroalaField(help_text='(job description)')
    posted_by = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=300, help_text='(job location)')
    category = models.ForeignKey(JobCategory)
    job_type = models.CharField(max_length=1, choices=TYPE)
    company_name = models.CharField(max_length=250)
    last_date = models.DateField(help_text='(last day of application)')
    requirements = FroalaField(help_text='(job description)')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['last_date']

watson.register(Job)

class JobApplication(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.IntegerField()
    current_company = models.CharField(max_length=300, help_text='<i class="ion-ios-information fa-lg"></i> optional', blank=True, null=True)
    portfolio_url = models.URLField(help_text='<i class="ion-ios-information fa-lg"></i> optional', blank=True, null=True)
    additional_information = models.TextField(help_text='<i class="ion-ios-information fa-lg"></i> add a cover letter or anything else you want to share', blank=True, null=True)
    resume = models.FileField(upload_to='Application_Documents', help_text='<i class="ion-ios-information fa-lg"></i> resume/CV (we prefer in pdf)')
    applied_at = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job)

    class Meta:
        ordering = ['-applied_at']

    def __str__(self):
        return '%s - %s' % (self.full_name, self.job,)
