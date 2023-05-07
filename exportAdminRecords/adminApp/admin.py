from django.contrib import admin
from .models import Image
from .admin_actions import export_to_csv


class ImageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'image_url', 'date_created')
    list_filter = ('user_id', 'date_created')
    actions = [export_to_csv]


admin.site.register(Image, ImageAdmin)
