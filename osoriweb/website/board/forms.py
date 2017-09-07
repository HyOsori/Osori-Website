from django import forms

from .models import FreePost, Comment

class FreePostForm(forms.ModelForm):

	class Meta:
		model = FreePost
		fields = ('title' , 'text',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)
