from django.contrib import admin

from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'views')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('views',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'article__title')
    list_filter = ('created_at',)
