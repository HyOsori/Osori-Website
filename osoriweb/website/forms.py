from django import forms

from .models import Inquiry

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InquiryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(InquiryForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Inquiry
		fields = ['name', 'email', 'title', 'content']

	name = forms.CharField(label='이름')
	email = forms.EmailField(label="이메일")
	title = forms.CharField(label="문의 제목")
	content = forms.CharField(widget=forms.Textarea, label = "문의 내용")


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user