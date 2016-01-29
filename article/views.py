from django.shortcuts import render

from django.http import HttpResponse
from article.models import Article
# Create your views here.


def article_list(request):
    #return HttpResponse('Hello world!')
    content = {}
    content['lists'] = Article.objects.all()
    return render(request, 'article_list.html', content)
