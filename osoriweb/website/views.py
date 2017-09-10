
from .forms import InquiryForm, UserForm
from .models import History

from django import forms
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class CustomPasswordChangeForm(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect': "비밀번호가 일치하지 않습니다, 다시 확인해주세요"}

    old_password = forms.CharField(required=True, label='이전 패스워드', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autofocus': True}), error_messages={'required': '이전 비밀번호를 입력해주세요'})

    new_password1 = forms.CharField(required=True, label='새 비밀번호', widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
            error_messages={'required': '새 비밀번호를 입력해주세요'})

    new_password2 = forms.CharField(required=True, label='비밀번호 확인', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), error_messages={'required': '비밀번호 확인이 일치하는지 확인해주세요'})


# Create your views here.

def index(request):
    return render(request, 'website/index.html', {})


def about(request):
    return redirect('about_introduce')


def about_introduce(request):
    return render(request, 'website/about_introduce.html', {})


def about_history(request):
    return render(request, 'website/about_history.html', {})


def about_location(request):
    return render(request, 'website/about_location.html', {})


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


def user_register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.profile.department = user_form.cleaned_data.get('department')
            user.profile.phone_number = user_form.cleaned_data.get('phone_number')
            user.profile.github_id = user_form.cleaned_data.get('github_id')
            user.save()
            messages.success(request, '회원 가입이 완료되었습니다.')
            return redirect('login/done')
        else:
            messages.error(request, '에러 발생')
            return render(request, 'registration/signup.html', {
                'user_form': user_form})
    else:
        user_form = UserForm()
        return render(request, 'registration/signup.html', {
            'user_form': user_form})


class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


@csrf_exempt
def history(request):
    if request.method == 'POST':
        year = request.POST['year']
        month = request.POST['month']
        content = request.POST['content']
        try:
            history = History(year=year, month=month, content=content)
            history.save()
        except:
            return HttpResponse('Fail')
        return HttpResponse("add history")

    if request.method == 'GET':
        return HttpResponse(History.objects.all())

    if request.method == 'DELETE':
        id = request.GET['id']
        try:
            history = History.objects.get(id=id)
        except:
            return HttpResponse('fail')
            history.delete()
        return HttpResponse("delete success")


def about_history(request):
    history = History.objects.all().order_by('year', 'month').reverse()
    return render(request, 'website/about_history.html', {'history': history})
