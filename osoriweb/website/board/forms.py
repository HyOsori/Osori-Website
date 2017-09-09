from django import forms

from .models import FreePost

class FreePostForm(forms.ModelForm):

	class Meta:
		model = FreePost
		fields = ('title' , 'text',)


