from django.shortcuts import render
from django.views import generic
from blog.models import *
from home.models import *
from management_board.models import *
from elite.mixins import *
from partners.models import *

class Home(MenuMixin, generic.TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Home, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['recent_post_list'] = Post.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['board_members'] = BoardMember.objects.all()
        context['partners'] = Partner.objects.all()
        return context