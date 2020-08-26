from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Author, Category, Post, Client, Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Client)
admin.site.register(Comment)