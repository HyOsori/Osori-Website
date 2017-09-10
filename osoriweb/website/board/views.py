from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Article
from .models import BoardType
from .forms import ArticleForm

ARTICLE_PER_PAGE = 1
RADIUS_OF_PAGINATOR = 1


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

    try:
        if request.GET['method'] is not None and request.GET['keyword'] is not None:
            method = request.GET['method']
            keyword = request.GET['keyword']
        else:
            method = ""
            keyword = ""
    except Exception:
        method = ""
        keyword = ""

    if method == 'author':
        articles = Article.objects.filter(created_date__lte=timezone.now())\
            .filter(type=board_type.value)\
            .filter(author__username__contains=keyword)\
            .order_by('-created_date')
    elif method == 'title':
        articles = Article.objects.filter(created_date__lte=timezone.now())\
            .filter(type=board_type.value)\
            .filter(title__contains=keyword)\
            .order_by('-created_date')
    else:
        articles = Article.objects.filter(created_date__lte=timezone.now()) \
            .filter(type=board_type.value) \
            .order_by('-created_date')

    paginator = Paginator(articles, ARTICLE_PER_PAGE)  # Show 10 contacts per page

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        articles = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        articles = paginator.page(page)

    page_number = int(page)

    page_min = page_number - RADIUS_OF_PAGINATOR
    page_max = page_number + RADIUS_OF_PAGINATOR

    if page_min < 0:
        page_min = 0

    if page_max > paginator.num_pages:
        page_max = paginator.num_pages

    return render(request, 'board/board.html', {
        'title': board_type.get_title(),
        'articles': articles,
        'current': page,
        'pages': range(page_min, page_max + 1),
        'board_name': board_type,
        'method': method,
        'keyword': keyword,
    })


def search_articles(request, **kwargs):

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

    try:
        if request.POST['method'] is not None:
            method = request.POST['method']
    except Exception:
        method = 'title'

    keyword = request.POST['keyword']

    if method == 'author':
        articles = Article.objects.filter(created_date__lte=timezone.now())\
            .filter(type=board_type.value)\
            .filter(author__username__contains=keyword)\
            .order_by('-created_date')
    else:
        articles = Article.objects.filter(created_date__lte=timezone.now())\
            .filter(type=board_type.value)\
            .filter(title__contains=keyword)\
            .order_by('-created_date')

    paginator = Paginator(articles, ARTICLE_PER_PAGE)  # Show 10 contacts per page

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        articles = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        articles = paginator.page(page)

    page_number = int(page)

    page_min = page_number - RADIUS_OF_PAGINATOR
    page_max = page_number + RADIUS_OF_PAGINATOR

    if page_min < 0:
        page_min = 0

    if page_max > paginator.num_pages:
        page_max = paginator.num_pages

    return render(request, 'board/board.html', {
        'title': board_type.get_title(),
        'articles': articles,
        'current': page,
        'pages': range(page_min, page_max + 1),
        'board_name': board_type,
        'method': method,
        'keyword': keyword
    })


def read_article(request, board_name, pk):

    try:
        board_type = BoardType(board_name)
    except Exception:
        board_type = BoardType.NOTI
        board_name = board_type.value

    articles = Article.objects.filter(created_date__lte=timezone.now()).\
        filter(type=board_name).\
        order_by('-created_date')

    count = articles.count()

    # Create list of articles which are right before and after the target article
    # This is done instead of get_object_or_404 because there was a need to find the index of the target article
    # To get the before and after articles of the target

    if count > 0:
        for idx in range(0, count):
            if articles[idx].pk == int(pk):  # Look for the target article
                break
    else:
        return render_to_response('board/no_result.html')

    try:
        before = None
        after = None

        article = articles[idx]  # Save the target article in the list
        if 0 < idx:
            before = articles[idx - 1]  # If the target article is not the first in the list, add the before article

        if idx < (count - 1):
            after = articles[idx + 1]  # If the target article is not the last in the list, add the last article.

        article.article_viewed()
    except Exception:
        return render_to_response('board/no_result.html')

    return render(request, 'board/read_article.html',
                  {
                      'article': article,
                      'before': before,
                      'after': after,
                      'board_name': board_name},
                  )


# TODO: 작성 권한이 있는지 확인, 폼 대신 html로 대체
@login_required
def create_article(request, board_name):

    try:
        board_type = BoardType(board_name)

    except Exception:
        board_type = BoardType.NOTI
        board_name = board_type.value

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.type = board_type
            article.save()
            return redirect('read_article', board_name=board_name, pk=article.pk)
    else:

        form = ArticleForm()

    return render(request, 'board/new_article.html', {'form': form, 'title': board_type.get_title()})


# TODO: 작성자가 맞는지 확인, 폼 대신 html로 대체
@login_required
def edit_article(request, board_name, pk):

    try:
        board_type = BoardType(board_name)

    except Exception:
        board_type = BoardType.NOTI
        board_name = board_type.value

    article = get_object_or_404(Article, type=board_name, pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.type = board_type
            article.save()
            return redirect('read_article', board_name=board_name, pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'board/edit_article.html', {'form': form, 'title': board_type.get_title()})


# TODO: 작성자가 맞는지 확인
@login_required
def remove_article(request, board_name, pk):
    article = get_object_or_404(Article, type=board_name, pk=pk)

    if article.author == request.user:
        article.delete()

    return redirect('select_articles')
