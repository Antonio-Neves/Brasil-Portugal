from django.shortcuts import render
from django.views.generic import TemplateView

from principal.models import Category, SubCategory, Article


def global_principal_content(request):
	"""
	Return context for use in all templates.
	"""
	global_principal_context = {
		'global_categories': Category.objects.all(),
		'global_subcategories': SubCategory.objects.all(),
		'global_articles': Article.objects.all()
	}

	return global_principal_context


class IndexView(TemplateView):

	def get(self, request, *args, **kwargs):
		context = {
			'categories': Category.objects.all(),
			'subcategories': SubCategory.objects.all(),
			'articles': Article.objects.all()
		}

		return render(request, 'principal/index.html', context)


def content(request):

	return render(request, 'principal/content.html')

