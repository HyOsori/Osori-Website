from django.db import models
from django.utils import timezone
from enum import Enum


class BoardType(Enum):
    NOTI = 'noti'   ## 공지
    INFO = 'info'   ## 정보
    FREE = 'free'   ## 자유

    ## 게시판의 제목
    def get_title(self):

        if self == BoardType.INFO:
            return '정보게시판'
        elif self == BoardType.FREE:
            return '자유게시판'
        else:   # 정보 게시판이나 자유 게시판이 아닌 경우 기본으로 공지 게시판
            return '공지게시판'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(default=0)
    text = models.TextField()
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    def article_viewed(self):
        self.view_count += 1
        self.save()