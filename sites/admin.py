from django.contrib import admin
from .models import Sites, SiteName

# Register your models here.
@admin.register(Sites)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('get_site_name', 'a_value', 'b_value')

    def get_site_name(self, obj):
        return obj.name
    get_site_name.short_description = 'Site Name'

@admin.register(SiteName)
class SiteNameAdmin(admin.ModelAdmin):
    pass