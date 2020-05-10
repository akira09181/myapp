from django import forms
from .models import Article,Inout

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索',max_length=100)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name')

class InoutForm(forms.ModelForm):
    class Meta:
        model = Inout
        fields = ('creterion_sell','creterion_buy','interval','volume')
