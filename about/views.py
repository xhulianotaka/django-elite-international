from django.shortcuts import render
from django.views import generic
from management_board.models import *
from elite.mixins import *

class About(MenuMixin, generic.TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(About, self).get_context_data(**kwargs)
        context['board_members'] = BoardMember.objects.all()
        return context