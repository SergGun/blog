from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django_ckeditor_5 import *
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'created_at')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
