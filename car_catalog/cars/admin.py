# cars/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Car
from django.urls import reverse


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'display_image', 'change_link')

    def display_image(self, obj):
        return format_html('<img src="{}" width="196" height="120" />', obj.image.url) if obj.image else ''

    display_image.short_description = 'Image'

    def change_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id] )
        return format_html("<a href='{}'>Edit</a>", url)

    change_link.short_description = 'Edit Link'

admin.site.register(Car, CarAdmin)
