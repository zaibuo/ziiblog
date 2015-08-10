#-*- coding=utf-8 -*-

from django.contrib import admin
from .models import Article, ArticleCategories, ArticleComment, ArticleTags, BlogInfo

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','articleCategories','created','updated')


class BlogInfoAdmin(admin.ModelAdmin):
	list_display = ('blogTitle', 'blogSubtitle',)

class ArticleTagsAdmin(admin.ModelAdmin):
	list_display = ('tags',)

class ArticleCategoriesAdmin(admin.ModelAdmin):
	list_display = ('categoryName',)

class ArticleCommentAdmin(admin.ModelAdmin):
	list_display = ('commentArticle', 'commentContent', 'commentUsername', 'commentTime')
# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(BlogInfo, BlogInfoAdmin)
admin.site.register(ArticleTags, ArticleTagsAdmin)
admin.site.register(ArticleCategories, ArticleCategoriesAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
