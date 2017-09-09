from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import InfoArticle, ArticleLikes
from .forms import InfoForm, SearchForm
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
    articles = InfoArticle.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    count = articles.count()

    # Create list of articles which are right before and after the target article
    # This is done instead of get_object_or_404 because there was a need to find the index of the target article
    # To get the before and after articles of the target
    before = 0 # Initialize
    now = 0
    after = 0
    for a in range(0, count):
        if articles[a].pk == int(pk): # Look for the target article
            break

    now = articles[a] # Save the target article in the list
    if a > 0 :
        before = articles[a-1] # If the target article is not the first in the list, add the before article

    if a != count - 1:
        after = articles[a+1] # If the target article is not the last in the list, add the last article.

    articleList = [before, now, after]
    now.view_count += 1
    now.save()
    return render(request, 'board/info_detail.html', {'articles' : articleList})

@login_required
def info_remove(request, pk):
    article = get_object_or_404(InfoArticle, pk=pk)
    if request.user == article.author or request.user.is_superuser:
        article.delete()
    return redirect('info_board')

@login_required
def info_like(request, pk):
    article = get_object_or_404(InfoArticle,pk = pk)
    liked_by_user = article.likes.filter(user = request.user)
    if not liked_by_user:
        article.likes.get_or_create(user=request.user, article=article)
    else:
        liked_by_user.delete()
    return redirect('info_detail', pk=article.pk)



def free_board(request):
    return render(request, 'board/free_board.html', {})