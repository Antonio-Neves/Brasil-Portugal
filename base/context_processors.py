from principal.models import Category, SubCategory, Article


def global_principal_content(request):
	"""
	Return context for use in all templates.
	"""
	global_principal_context = {
		'global_categories': Category.objects.all(),
		'global_subcategories': SubCategory.objects.all(),
		'global_articles': Article.objects.filter(article_status='1')
	}

	return global_principal_context