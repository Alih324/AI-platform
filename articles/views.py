from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm, CommentForm
from .models import Article


def articles_list(request):
    articles = Article.objects.select_related('author')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article.objects.select_related('author'), pk=pk)
    Article.objects.filter(pk=article.pk).update(views=F('views') + 1)
    article.refresh_from_db(fields=['views'])

    comment_form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to comment.')
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment was added.')
            return redirect('article_detail', pk=article.pk)

    comments = article.comments.select_related('author')
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created successfully.')
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/add_article.html', {'form': form})


@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.author != request.user and not request.user.is_staff:
        messages.error(request, 'You can only edit your own articles.')
        return redirect('article_detail', pk=article.pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully.')
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})
