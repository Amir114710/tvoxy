from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('' , ArticleListView.as_view() , name='article_list'),
    path('blog_detail/<str:slug>' , ArticleDetailView.as_view() , name='article_detail'),
]