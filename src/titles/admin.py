from django.contrib import admin

from .models import Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ('text', 'picks', 'appearances')
    search_fields = ('text', )
    fieldsets = (('General', {'fields': ('text', )}), )


admin.AdminSite.site_title = admin.AdminSite.site_header = 'Admin Panel'

admin.site.register(Title, TitleAdmin)
