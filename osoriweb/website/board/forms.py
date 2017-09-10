from django import forms
from .models import Article
from .models import BoardType
from django_summernote.widgets import SummernoteWidget


# 게시글 폼
class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(ArticleForm,self).__init__(*args,**kwargs)


    class Meta:
        model = Article
        fields = ('title', 'text',)  # 제목과 내용을 입력 가능하도록 설정

    title = forms.CharField(required=True, label="제목")
    text = forms.CharField(widget=SummernoteWidget, label="내용")


