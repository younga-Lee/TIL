from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all() #전체데이터 조회
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)

def new(request): #사용자가 입력을 받을 페이지 렌더링
    return render(request, 'articles/new.html')