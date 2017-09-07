from django.shortcuts import render, get_object_or_404, redirect
from .models import FreePost, Comment
from .forms import FreePostForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sys


# Create your views here.
def board(request):
    return redirect('noti_board')

def noti_board(request):
    return render(request, 'board/noti_board.html', {})

def info_board(request):
    return render(request, 'board/info_board.html', {})

def free_board(request):
	articles = FreePost.objects.filter(published_date__lte=timezone.now()).order_by('pk')
	paginator = Paginator(articles, 25)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)	
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'board/free_board.html', {'posts' : posts})

def free_new(request):
	if request.method == "POST":
		form = FreePostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish()
			return redirect('free_detail', pk=post.pk)
	else:
		form = FreePostForm()
	return render(request, 'board/free_new.html', {'form': form})

def free_detail(request, pk):
    post = get_object_or_404(FreePost, pk=pk)
    if request.method == "POST":
        form = FreePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FreePostForm(instance=post)
        post.view_count +=1
        post.save()
    return render(request, 'board/free_detail.html', {'form': form, 'post':post})

def free_delete(request, pk):
	post = get_object_or_404(FreePost, pk=pk)
	if post.author == request.user :
		post.delete()
	else:
		return redirect('free_detail', pk=post.pk)
	return redirect('free_board')

def post_detail(request, pk):
	post = get_object_or_404(FreePost, pk=pk)
	post.view_count +=1
	post.save()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			print("Goodbye cruel world!", file=sys.stderr)
			comment = form.save(commit=False)
			comment.author = request.user
			comment.published_date = timezone.now()
			comment.publish()
			return redirect('free_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'board/post_detail.html', {'post' : post})


