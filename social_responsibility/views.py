from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class SocialResponsibility(MenuMixin, generic.TemplateView):
    template_name = 'social_responsibility/social_responsibility.html'