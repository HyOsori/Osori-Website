from django import forms

from .models import Inquiry

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
