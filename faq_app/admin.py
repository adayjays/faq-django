from django.contrib import admin
from .models import Category, FAQ, Article
from .forms import ArticleForm,FAQForm

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

class FAQAdmin(admin.ModelAdmin):
    form = FAQForm

admin.site.register(Category)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(Article,ArticleAdmin)
