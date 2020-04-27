from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ArticleListView(TemplateView):
    template_name = "articles/articles_list.html"

class ArticleCreateView(TemplateView):
    template_name = "articles/articles_create.html"
