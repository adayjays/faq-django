from django.urls import path, re_path
from . import views

urlpatterns = [
    path('faq/', views.faq_page, name='faq_page'),
    path('article/<slug:article_id>/', views.view_article, name='view_article'),
    path('faq/<int:faq_id>/', views.view_faq, name='view_faq'),
    path('posts/<slug:article_slug>/', views.view_articles, name='view_articles_with_slug'),
    path('posts/', views.view_articles, name='view_articles'),
    path('search/', views.search, name='search'),
    re_path('^', views.faq_page, name='faq_page'),  # Catch-all pattern should be placed at the end
]
