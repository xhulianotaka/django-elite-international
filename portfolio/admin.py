from django.contrib import admin
from portfolio.models import *
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
admin.site.register(PortfolioCategory, CategoriesAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_at', 'user', 'category', 'num_views')
    search_fields = ('title', 'description',)
    exclude = ('user',)
    raw_id_fields = ('category',)
    readonly_fields = ('num_views',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        obj.slug = slugify(obj.title)
        super(PortfolioAdmin, self).save_model(request, obj, form, change)
admin.site.register(Portfolio, PortfolioAdmin)
