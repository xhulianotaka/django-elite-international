from django.contrib import admin
from blog.models import *
from django.template.defaultfilters import slugify

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'description',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        obj.slug = slugify(obj.name)
        super(CategoriesAdmin, self).save_model(request, obj, form, change)

admin.site.register(Category, CategoriesAdmin)

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'user', 'created_at', 'updated_at', 'num_views')
    list_filter = ('category', 'user',)
    search_fields = ('title', 'description',)
    exclude = ('user',)
    readonly_fields = ('num_views',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        obj.slug = slugify(obj.title)
        super(PostsAdmin, self).save_model(request, obj, form, change)

admin.site.register(Post, PostsAdmin)
