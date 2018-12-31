from django.contrib import admin

# Register your models here.
from .models import NewsLink, Startup, Tag

admin.site.register(NewsLink)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
