from django.contrib import admin
from home.models import *

admin.site.site_header = 'Elite Administration'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'posted_by', 'posted_at')
    search_fields = ('author', 'description',)
    exclude = ('posted_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.posted_by = request.user
        super(TestimonialAdmin, self).save_model(request, obj, form, change)

admin.site.register(Testimonial, TestimonialAdmin)
