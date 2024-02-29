from django.contrib import admin
from .models import Category, News, Comment
# Register your models here.
from django.utils.html import format_html


class CommentInline(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width=50px/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    inlines = [
        CommentInline,
    ]
    list_display = ("title", "name_author", 'image', 'image_tag', "status", "date")
    readonly_fields = ['image_tag', ]
    list_filter = ("name_author", "category", "status", "date")
    list_editable = ("status",)





admin.site.register(Category)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)