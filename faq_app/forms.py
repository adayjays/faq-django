from django import forms
from .models import Article, FAQ
from .widgets import JoditWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': JoditWidget(),
        }

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        answer = {
            'answer': JoditWidget(),
        }
