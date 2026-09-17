from django.contrib import admin
from .models import Ad, Link

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'destination_url', 'ad')
    list_filter = ('ad',)