from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import InfoArticle, InfoComment, CommentLikes
from .forms import InfoForm, InfoCommentForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def board(request):
    return redirect('noti_board')

def noti_board(request):
    return render(request, 'board/noti_board.html', {})

def info_board(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            arg = form.cleaned_data
            key = arg.get('searchKey')
            posts = InfoArticle.objects.filter(created_date__lte = timezone.now()).filter(title__icontains = key).order_by('-created_date')
    else:
        posts = InfoArticle.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
        form = SearchForm()

    paginator = Paginator(posts, 25) # Show 25 articles per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'board/info_board.html', {'articles' : articles, 'form' : form})

@login_required
def info_new(request):
	if request.method == "POST":
	    form = InfoForm(request.POST)
	    if form.is_valid():
	        article = form.save(commit=False)
	        article.author = request.user
	        article.save()
	        return redirect('info_detail', pk=article.pk)
	else:
	    form = InfoForm()
	return render(request, 'board/info_new.html', {'form': form})

@login_required
def info_edit(request, pk):
    article = get_object_or_404(InfoArticle, pk=pk)
    if request.method == "POST":
        form = InfoForm(request.POST, instance = article)
        if form.is_valid():
            article = form.save(commit = False)
            article.author = request.user
            article.save()
            return redirect('info_detail', pk = article.pk)
    else:
        form = InfoForm(instance = article)
    return render(request, 'board/info_new.html', {'form': form})

def info_detail(request, pk):
    articleses = InfoArticle.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    count = articleses.count()
    before = 0
    now = 0
    after = 0
    for a in range(0, count):
        if articleses[a].pk == int(pk):
            break

    now = articleses[a]
    if a > 0 :
        before = articleses[a-1]

    if a != count - 1:
        after = articleses[a+1]

    articles = [before, now, after]
    if request.method == "POST":
        form = InfoCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = now
            comment.author = request.user
            comment.save()
            return redirect('info_detail', pk=now.pk)
    else:
        form = InfoCommentForm()
        now.view_count += 1
        now.save()
    return render(request, 'board/info_detail.html', {'articles' : articles})

@login_required
def info_remove(request, pk):
    article = get_object_or_404(InfoArticle, pk=pk)
    if request.user == article.author or request.user.is_superuser:
        article.delete()
    return redirect('info_board')

@login_required
def info_comment_remove(request, pk):
    comment = get_object_or_404(InfoComment, pk = pk)
    article = comment.article
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
    return redirect('info_detail', pk=article.pk)

@login_required
def info_like(request, pk):
    comment = get_object_or_404(InfoComment,pk = pk)
    liked_by_user = comment.likes.filter(user = request.user)
    if not liked_by_user:
        comment.likes.get_or_create(user=request.user, comment=comment)
    else:
        liked_by_user.delete()
    return redirect('info_detail', pk=comment.article.pk)



def free_board(request):
    return render(request, 'board/free_board.html', {})