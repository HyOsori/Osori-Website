from django import forms

from .models import InfoArticle, InfoComment
from django_summernote.widgets import SummernoteWidget

class InfoForm(forms.ModelForm):

    class Meta:
        model = InfoArticle
        fields = ('title', 'text',)
        widgets = {
        	'text' : SummernoteWidget(),
        }


class InfoCommentForm(forms.ModelForm):

    class Meta:
        model = InfoComment
        fields = ('author', 'text',)