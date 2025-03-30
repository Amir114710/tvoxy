from django.shortcuts import render
from django.views.generic import ListView , DetailView

from blog.models import Article

class ArticleListView(ListView):
    template_name = 'blog/blog.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 6
    def get_queryset(self):
          return Article.objects.filter(is_publish=True)
    
class ArticleDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Article
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] =  Article.objects.all()[:3]
        return context
