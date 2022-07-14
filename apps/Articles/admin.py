from django.contrib import admin
from .models import Post, Comment, Category, Tag


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)
    search_fields = ('title',)
    filter_horizontal = ('tags',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
