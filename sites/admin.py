from django.contrib import admin
from .models import Sites, SiteName

# Register your models here.
@admin.register(Sites)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(SiteName)
class SiteNameAdmin(admin.ModelAdmin):
    pass