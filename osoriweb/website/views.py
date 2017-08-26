from django.shortcuts import render, redirect
from .forms import InquiryForm

from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
	return redirect('about_introduce')

def about_introduce(request):
	return render(request, 'website/about_introduce.html',{})

def about_history(request):
	return render(request, 'website/about_history.html',{})

def about_location(request):
	return render(request, 'website/about_location.html',{})

def contact(request):
	if request.method == "POST":
		form = InquiryForm(request.POST)
		if form.is_valid():
			inquiry = form.save()
			messages.success(request, '문의사항이 성공적으로 전달되었습니다.')
			return redirect('contact')
	else:
		form = InquiryForm()
	return render(request, 'website/contact.html', {'form': form})