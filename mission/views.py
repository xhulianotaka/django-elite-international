from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class Mission(MenuMixin, generic.TemplateView):
    template_name = 'mission/mission.html'