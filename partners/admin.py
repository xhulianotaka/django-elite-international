from django.contrib import admin
from partners.models import *
from django.template.defaultfilters import slugify

class PartnerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'description')
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        obj.slug = slugify(obj.name)
        super(PartnerAdmin, self).save_model(request, obj, form, change)
admin.site.register(Partner, PartnerAdmin)