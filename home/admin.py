from django.contrib import admin
from .models import Music, SubMusic

admin.site.register(SubMusic)

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display=['title','style','content','audio']
    list_per_page = 3