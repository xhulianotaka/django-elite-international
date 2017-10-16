from watson.views import SearchView
from .mixins import *

class SearchViewCustom(MenuMixin, SearchView):
    paginate_by = 6
    template_name = 'generic_search.html'