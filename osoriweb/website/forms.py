from django import forms

from .models import Inquiry, Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import *
from django.forms.models import model_to_dict, fields_for_model

class InquiryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(InquiryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'title', 'content']

    name = forms.CharField(label='이름', widget=forms.TextInput(attrs={'class':'ui input'}))
    email = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'class':'ui input'}))
    title = forms.CharField(label="문의 제목", widget=forms.TextInput(attrs={'class':'ui input'}))
    content = forms.CharField(widget=forms.Textarea, label = "문의 내용")


class UserForm(UserCreationForm):

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    username = forms.RegexField(label="아이디", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="문자 숫자 포함 30자 이하, 특수문자 @/./+/-/_ ",
                                error_messages={
                                    'invalid': "This value may contain only letters, numbers and "
                                               "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'required': 'true',
                                }))

    password1 = forms.CharField(label="비밀번호",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'required': 'true',
                                }))
    password2 = forms.CharField(label="비밀번호 확인",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'required': 'true',
                                }))

    email = forms.EmailField(label='이메일', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'required': 'True',
        }
    ))

    department = forms.CharField(label='전공', required=True, max_length=15)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    error_messages={
                                        'invalid': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})
    github_id = forms.RegexField(label="Github", max_length=30,
                                 regex=r'^[\w.@+-]+$',
                                 error_messages={
                                     'invalid': "This value may contain only letters, numbers and "
                                                "@/./+/-/_ characters."},
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'required': 'true',
                                 }))

    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2', 'department', 'phone_number', 'github_id')

    def clean_password1(self):

        password1 = self.cleaned_data.get("password1")

        try:  # FIXME: settings.py에서 AUTH_PASSWORD_VALIDATORS가 적용되지 않아 임시방편으로 유효성 검증
            validator = UserAttributeSimilarityValidator()
            validator.validate(password1)

            validator = MinimumLengthValidator()
            validator.validate(password1)

            validator = CommonPasswordValidator()
            validator.validate(password1)

            validator = NumericPasswordValidator()
            validator.validate(password1)
        except Exception as error:
            raise error

        return password1

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('department', 'phone_number', 'github_id')
