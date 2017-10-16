from django.shortcuts import render
from django.views import generic
from management_board.models import *
from elite.mixins import *
from partners.models import *

class Management(MenuMixin, generic.TemplateView):
    template_name = 'management_board/management_board.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Management, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['board_members'] = BoardMember.objects.all()
        context['partners'] = Partner.objects.all()
        return context

class BoardMemberDetail(MenuMixin, generic.DetailView):
    model = BoardMember
    context_object_name = 'member'
    template_name = 'management_board/board_member_detail.html'