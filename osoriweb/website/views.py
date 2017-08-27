from django.shortcuts import render, redirect
from .forms import InquiryForm

from django.contrib import messages

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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



class CreateUserView(CreateView):
	template_name = 'registration/signup.html'
	form_class =  CreateUserForm
	success_url = reverse_lazy('create_user_done')


class RegisteredView(TemplateView):
	template_name = 'registration/signup_done.html'



def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'registration/change_password.html', { 'form': form})


def change_profile(request):
	return render(request,'registration/change_profile.html',{})
