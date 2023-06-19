from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_date', 'display_image')
    search_fields = ('title', 'uploaded_by__username')
    list_filter = ('created_date', 'uploaded_by')
    date_hierarchy = 'created_date'
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return 'No image'

    display_image.short_description = 'Image Preview'
