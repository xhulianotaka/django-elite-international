from django.shortcuts import render
from django.views import generic
from gallery.models import *
from elite.mixins import *

class ImageGallery(MenuMixin, generic.ListView):
    model = ImageGallery
    context_object_name = 'gallery_items'
    template_name = 'gallery/image_gallery.html '
