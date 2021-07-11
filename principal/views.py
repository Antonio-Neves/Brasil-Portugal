from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from principal.models import Category, SubCategory, Article


# --- Home Page --- #
class IndexView(TemplateView):
	template_name = 'principal/index.html'


# --- Categories --- #
class CategoryDetailView(DetailView):
	model = Category
	slug_field = 'category_slug'
	template_name = 'principal/category-detail.html'


# --- SubCategories --- #
class SubCategoryDetailView(DetailView):
	model = SubCategory
	slug_field = 'sub_category_slug'
	template_name = 'principal/subcategory-detail.html'


# --- Articles --- #
class ArticleDetailView(DetailView):
	model = Article
	slug_field = 'article_slug'
	template_name = 'principal/article-detail.html'
	# context_object_name = 'article'
