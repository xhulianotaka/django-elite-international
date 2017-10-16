from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class HumanResources(MenuMixin, generic.TemplateView):
    template_name = 'human_resources/human_resources.html'