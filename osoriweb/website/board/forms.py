from django import forms
from .models import Article
from .models import BoardType
from django_summernote.widgets import SummernoteWidget


# 게시글 폼
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',)  # 제목과 내용을 입력 가능하도록 설정

        title = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        type = forms.TypedChoiceField(choices=BoardType.choices(), coerce=str)
        message = forms.CharField(widget=forms.Textarea)

        widgets = {
            'text': SummernoteWidget()
        }
