from django.shortcuts import render
from django.views.generic import TemplateView

from principal.models import Category


class IndexView(TemplateView):

	def get(self, request, *args, **kwargs):
		context = {'categories': Category.objects.all()}

		print(context)

		return render(request, 'principal/index.html', context)


def content(request):

	return render(request, 'principal/content.html', {})
