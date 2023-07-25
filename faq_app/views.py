from django.shortcuts import render, get_object_or_404
from .models import Category, FAQ, Article
from django.db.models import Q

def faq_page(request):
    categories = Category.objects.all()
    faqs = FAQ.objects.all()
    articles = Article.objects.all()
    return render(request, 'faq.html', {'categories': categories, 'faqs': faqs, 'articles': articles})

def view_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    return render(request, 'faq_detail.html', {'faq': faq})

def view_article(request, article_id):
    article = get_object_or_404(Article, slug=article_id)
    return render(request, 'article_detail.html', {'article': article})

def view_articles(request, article_slug=None):
    if article_slug:
        latest_article = get_object_or_404(Article, slug=article_slug)
    else:
        latest_article = Article.objects.latest('created_at')

    all_articles = Article.objects.all()
    article_categories = Category.objects.all()

    return render(request, 'articles.html', {
        'latest_article': latest_article,
        'all_articles': all_articles,
        'article_categories': article_categories,
    })

def search(request):
    search_query = request.GET.get('q')
    if search_query:
        articles = Article.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
        faqs = FAQ.objects.filter(
            Q(question__icontains=search_query) |
            Q(answer__icontains=search_query)
        )
    else:
        articles = Article.objects.none()
        faqs = FAQ.objects.none()

    return render(request, 'search_results.html', {'articles': articles, 'faqs': faqs})
