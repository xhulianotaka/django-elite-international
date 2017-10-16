from django.contrib import admin
from django.template.defaultfilters import slugify
from management_board.models import *

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'created_at', 'created_by')
    search_fields = ('first_name', 'last_name', 'position',)
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        member_full_name = '%s %s' % (obj.first_name, obj.last_name)
        obj.slug = slugify(member_full_name)
        super(BoardMemberAdmin, self).save_model(request, obj, form, change)

admin.site.register(BoardMember, BoardMemberAdmin)

class SkillsMemberAdmin(admin.ModelAdmin):
    list_display = ('skill', 'evaluation', 'member', 'created_at', 'created_by')
    list_filter = ('member',)
    search_fields = ('skill', 'evaluation',)
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super(SkillsMemberAdmin, self).save_model(request, obj, form, change)

admin.site.register(SkillsMember, SkillsMemberAdmin)
