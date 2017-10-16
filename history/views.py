from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class History(MenuMixin, generic.TemplateView):
    template_name = 'history/history.html'