from django.shortcuts import render
from django.views import generic
from elite.mixins import *

class Coorporate(MenuMixin, generic.TemplateView):
    template_name = 'coorporate_governance/coorporate.html'