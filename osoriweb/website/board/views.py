from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Article
from .models import BoardType
from .forms import ArticleForm


def select_articles(request, **kwargs):

    try:
        if kwargs['board_name'] is not None:
            board_type = BoardType(kwargs['board_name'])
    except Exception:
        board_type = BoardType.NOTI

    try:
        if kwargs['page'] is not None:
            page = kwargs['page']
    except Exception:

        page = 1

    articles = Article.objects.filter(created_date__lte=timezone.now()).filter(type=board_type).order_by('-created_date')

    paginator = Paginator(articles, 10)  # Show 10 contacts per page

    try:
        pagination = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pagination = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pagination = paginator.page(paginator.num_pages)
    print(board_type)
    return render(request, 'board/board.html', {
        'title': board_type.get_title(),
        'articles': articles,
        'pagination': pagination,
        'board_name': board_type
    })


def read_article(request, board_name, pk):

    try:
        board_type = BoardType(board_name)
    except Exception:
        board_type = BoardType.NOTI

    try:
        article = get_object_or_404(Article, type=board_type, pk=pk)
        article.article_viewed()
    except:
        return render_to_response('board/no_result.html')

    return render(request, 'board/read_article.html', {'article': article})


# TODO: 작성 권한이 있는지 확인, 폼 대신 html로 대체
@login_required
def create_article(request, board_name):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('read_article', board_name=board_name, pk=article.pk)
    else:
        form = ArticleForm()

    return render(request, 'board/new_article.html', {'form': form})


# TODO: 작성자가 맞는지 확인, 폼 대신 html로 대체
@login_required
def edit_article(request, board_name, pk):
    article = get_object_or_404(Article, pk=pk)

    if not article.author == request.user:
        return redirect('read_article', board_name=board_name, pk=article.pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('read_article', board_name=board_name, pk=article.pk)
    else:
        return render(request, 'board/edit_article.html', {'article': article})


# TODO: 작성자가 맞는지 확인
@login_required
def remove_article(request, board_name, pk):
    article = get_object_or_404(Article, type=board_name, pk=pk)

    if article.author == request.user:
        article.delete()

    return redirect('select_articles')