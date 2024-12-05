from django.contrib import admin
from home.models import Settings 

class SettingsAdmin(admin.ModelAdmin):
    list_display=['title','image_tag']
    readonly_fields=('image_tag',)


admin.site.register(Settings,SettingsAdmin)
