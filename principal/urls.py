from django.urls import path

from principal.views import IndexView, content


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('conteudo/', content, name='content')
]
