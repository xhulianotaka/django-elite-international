from django.shortcuts import render
from django.views import generic
from portfolio.models import *
from taggit.models import *
from elite.mixins import *
from django.db.models import F

class PortfolioList(MenuMixin, generic.ListView):
    model = Portfolio
    context_object_name = 'apps'
    paginate_by = 6
    template_name = 'portfolio/portfolio_list.html'

class PortfolioDetail(MenuMixin, generic.DetailView):
    model = Portfolio
    context_object_name = 'app'
    template_name = 'portfolio/portfolio_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PortfolioDetail, self).get_context_data(**kwargs)
        project = Portfolio.objects.get(slug=self.kwargs['slug'])
        project.num_views = F('num_views') + 1
        project.save()
        return context

class CategoryDetail(MenuMixin, generic.DetailView):
    model = PortfolioCategory
    context_object_name = 'category'
    template_name = 'portfolio/category_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['category_list'] = PortfolioCategory.objects.all()
        return context

class TagDetail(MenuMixin, generic.DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'portfolio/tag_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TagDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['apps_list'] = Portfolio.objects.filter(tags__name=self.kwargs['slug'])
        return context