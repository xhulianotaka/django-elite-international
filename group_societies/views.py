from django.shortcuts import render
from django.views import generic
from portfolio.models import *
from elite.mixins import *

class GroupSocities(MenuMixin, generic.ListView):
    model = Portfolio
    context_object_name = 'apps'
    paginate_by = 6
    template_name = 'group_socities/group_socities.html'