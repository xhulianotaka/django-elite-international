from django.contrib import admin
from gallery.models import *

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_by', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('description',)
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        super(ImageGalleryAdmin, self).save_model(request, obj, form, change)

admin.site.register(ImageGallery, ImageGalleryAdmin)
