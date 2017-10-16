from django.shortcuts import render
from django.views import generic
from blog.models import *
from taggit.models import *
from django.db.models import Q
from elite.mixins import *
from django.utils.decorators import method_decorator
from django.db.models import F

class Blog(MenuMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/blog_list.html'

class BlogDetail(MenuMixin, generic.DetailView):
    model = Post
    context_object_name = 'post'
    count_hit = True
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogDetail, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=self.kwargs['slug'])
        post.num_views = F('num_views') + 1
        post.save()
        context['categories_list'] = Category.objects.all()
        context['recent_post_list'] = Post.objects.all()
        context['tags_list'] = Tag.objects.filter(taggit_taggeditem_items__content_type__model='post')
        return context

class CategoryDetail(MenuMixin, generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'blog/category_detail.html'

class TagDetail(MenuMixin, generic.DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'blog/tag_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TagDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['post_list'] = Post.objects.filter(tags__name=self.kwargs['slug'])
        return context
