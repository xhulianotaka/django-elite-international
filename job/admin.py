from django.contrib import admin
from job.models import *
from django.template.defaultfilters import slugify
from django.contrib.admin.utils import flatten_fieldsets

class JobCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'description',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        obj.slug = slugify(obj.name)
        super(JobCategoriesAdmin, self).save_model(request, obj, form, change)

admin.site.register(JobCategory, JobCategoriesAdmin)

class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'posted_by', 'posted_at', 'job_type', 'last_date',)
    search_fields = ('title', 'description',)
    exclude = ('posted_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.posted_by = request.user

        obj.slug = slugify(obj.title)
        super(JobAdmin, self).save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'applied_at')
    list_filter = ('full_name',)
    search_fields = ('full_name',)

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

admin.site.register(JobApplication, JobApplicationAdmin)