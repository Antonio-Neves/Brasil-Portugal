from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from principal.models import Category, SubCategory, Article


class ArticleAdmin(SummernoteModelAdmin):
	list_display = ['article_name', 'article_cat', 'article_status']
	list_filter = ('article_cat', 'article_status')
	search_fields = ['article_name']
	prepopulated_fields = {'article_slug': ('article_name',)}
	summernote_fields = ('article_content',)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Article, ArticleAdmin)
