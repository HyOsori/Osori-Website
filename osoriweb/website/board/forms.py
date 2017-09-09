from django import forms

from .models import InfoArticle
from django_summernote.widgets import SummernoteWidget

class InfoForm(forms.ModelForm):

    class Meta:
        model = InfoArticle
        fields = ('title', 'text',)
        widgets = {
        	'text' : SummernoteWidget(),
        }

class SearchForm(forms.Form):
	searchKey = forms.CharField(max_length = 30)