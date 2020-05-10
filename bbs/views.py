from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm
from .forms import InoutForm
from .models import Inout
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
from .models import Calc
import io



def index(request):
    searchForm = SearchForm(request.GET)
    inoutForm=InoutForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles= Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()
    context = {
		'message': 'Welcome my system',
		'articles':articles,
        'searchForm': searchForm,
        'inoutForm':inoutForm,
    }
    return render(request, 'bbs/index.html' , context)
def detail(request,id):
    article = get_object_or_404(Article,pk=id)
    context = {
        'message':'Show Article'+str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html',context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }

    return render(request,'bbs/new.html',context)

def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
    context = {
        'message': 'Create article '+str(article.id),
        'article':article,
    }
    return render(request,'bbs/detail.html',context)

def edit(request,id):
    article = get_object_or_404(Article,pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message':'Edit Article '+str(id),
        'article': article,
        'articleForm':articleForm,
    }
    return render(request, 'bbs/edit.html',context)

def update(request,id):
    if request.method == 'POST':
        article = get_object_or_404(Article,pk=id)
        articleForm = ArticleForm(request.POST,instance=article)
        if articleForm.is_valid():
            articleForm.save()

    context = {
        'message':'Update Article　'+str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html',context)
def delete(request,id):
    article = get_object_or_404(Article,pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete Article '+ str(id),
        'articles':articles,
    }
    return render(request, 'bbs/index.html' , context)
def calc(request):
    
    inouts = Inout.objects.all()
    bit = pd.read_csv('../bitcoin.csv')
    bit=bit.iloc[::-1]
    itv=int(request.POST['interval'])
    v=int(request.POST['volume'])
    x=bit.Id
    y=bit.Close
    plt.plot(x,y)


    #plt.tight_layout()
    #buf=io.BytesIO()
    #plt.savefig(buf,format='svg',bbox_inches='tight')
    #svg=buf.getvalue()
    #buf.close()
    #plt.cla()
    bot=int(request.POST['creterion_buy'])
    top=int(request.POST['creterion_sell'])
    total=0
    stock=0
    count=0
    high=0
    hstock=0
    for i in range(0,len(bit),itv+1):
        
        if bit.Close[len(bit)-i-1] <=bot:
            total-=(bit.Close[len(bit)-i-1])*v
            stock+=(1*v)
        elif bit.Close[len(bit)-i-1] >=top:
            total+=bit.Close[len(bit)-i-1]*stock
            stock=0
        else:
            pass
        count+=1
        
        if high>total:
            high=total
            hstock=stock
    total+=bit.Close[len(bit)-1]*stock
    stock=0
    
    Calc.max_stock=hstock
    Calc.max_usd=high
    Calc.gains=total
    print(Calc.gains)
    calcs=Calc.objects.all()
    context = {
        
        'calcs':calcs,
        'max_usd':int(high),
        'max_stock':int(hstock),
        'gains':int(total),

    }
   
    
   
    return render(request, 'bbs/result.html',context,)