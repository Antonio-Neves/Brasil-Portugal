from django.urls import path

from principal.views import (
	IndexView,
	CategoryDetailView,
	SubCategoryDetailView,
	ArticleDetailView,
)

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('category/<slug:slug>/',
		 CategoryDetailView.as_view(), name='category-detail'),
	path('subcategory/<slug:slug>/',
		 SubCategoryDetailView.as_view(), name='subcategory-detail'),
	path('article/<slug:slug>/',
		 ArticleDetailView.as_view(), name='article-detail'),
]
