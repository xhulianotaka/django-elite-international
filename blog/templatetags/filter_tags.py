from django import template
from blog.models import *
from portfolio.models import *
from job.models import *
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    d = request.GET.copy()
    d[field] = value

    return d.urlencode()

@register.simple_tag
def url_delete(request, field):
    d = request.GET.copy()
    del d[field]

    return d.urlencode()

@register.assignment_tag
def get_next_app(app_id):
    app = Portfolio.objects.get(id=app_id)
    try:
        next_app = app.get_next_by_created_at()
    except Portfolio.DoesNotExist:
        next_app = None

    return next_app

@register.assignment_tag
def get_previous_app(app_id):
    app = Portfolio.objects.get(id=app_id)
    try:
        previous_app = app.get_previous_by_created_at()
    except Portfolio.DoesNotExist:
        previous_app = None

    return previous_app

@register.assignment_tag
def get_previous_post(post_id):
    post = Post.objects.get(id=post_id)
    try:
        previous_blog = post.get_previous_by_created_at()
    except Post.DoesNotExist:
        previous_blog = None

    return previous_blog

@register.assignment_tag
def get_next_post(post_id):
    post = Post.objects.get(id=post_id)
    try:
        next_blog = post.get_next_by_created_at()
    except Post.DoesNotExist:
        next_blog = None

    return next_blog

@register.assignment_tag
def get_previous_job(job_id):
    job = Job.objects.get(id=job_id)
    try:
        previous_job = job.get_previous_by_posted_at()
    except Job.DoesNotExist:
        previous_job = None

    return previous_job

@register.assignment_tag
def get_next_job(job_id):
    job = Job.objects.get(id=job_id)
    try:
        next_job = job.get_next_by_posted_at()
    except Job.DoesNotExist:
        next_job = None

    return next_job
