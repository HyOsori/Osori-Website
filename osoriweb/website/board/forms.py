from django import forms
from .models import Article

# 게시글 폼
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',) # 제목과 내용을 입력 가능하도록 설정