from django import forms

from .models import Inquiry, UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import model_to_dict, fields_for_model

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



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'password', 'email', 'first_name', 'last_name')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        extends = ['user',]
        fields = (''department', 'phone_number', 'github_id')