from django import forms

from .models import FreePost, Comment

class FreePostForm(forms.ModelForm):

	class Meta:
		model = FreePost
		fields = ('title' , 'text',)

class CommentForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea,label='')
	class Meta:
		model = Comment
		fields = ('text',)
