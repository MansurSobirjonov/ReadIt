from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateCommentForm
from .models import Post, Category, Tag


def home(request):
    articles = Post.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def blog(request):
    articles = Post.objects.all()
    search = request.GET.get('search')
    if search:
        articles = articles.filter(title__icontains=search)
    cat = request.GET.get('cat')
    if cat:
        articles = articles.filter(categories__category__exact=cat)
    tag = request.GET.get('tag')
    if tag:
        articles = articles.filter(tags__tags__exact=tag)
    context = {
        'articles': articles,
        'search': search,
    }
    return render(request, 'blog.html', context)


def blog_single(request, pk):
    article = Post.objects.get(id=pk)
    last_2_articles = Post.objects.order_by('-id')[:2]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    form = CreateCommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        com = form.save(commit=False)
        com.post = article
        com.save()
    context = {
        'article': article,
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'form': form,
    }
    return render(request, 'blog-single.html', context)
