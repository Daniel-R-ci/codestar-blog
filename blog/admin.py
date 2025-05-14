from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved')
    list_filter = ('approved',)
