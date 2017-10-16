from portfolio.models import *

class MenuMixin(object):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuMixin, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['category_list'] = PortfolioCategory.objects.order_by('-created_at')
        return context