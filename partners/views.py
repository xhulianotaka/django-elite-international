from django.shortcuts import render
from django.views import generic
from partners.models import *
from elite.mixins import *

class PartnerDetail(MenuMixin, generic.DetailView):
    model = Partner
    context_object_name = 'partner'
    template_name = 'partners/partner_detail.html'