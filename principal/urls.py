from django.urls import path

from principal.views import index, content


urlpatterns = [
	path('', index, name='index'),
	path('conteudo/', content, name="content")
]
