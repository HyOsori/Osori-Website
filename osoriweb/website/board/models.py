from django.db import models
from django.utils import timezone
from enum import Enum
import inspect


class BoardType(Enum):
    NOTI = 'noti'   # 공지
    INFO = 'info'   # 정보
    FREE = 'free'   # 자유

    # 게시판의 제목
    def get_title(self):

        if self == BoardType.INFO:
            return '정보게시판'
        elif self == BoardType.FREE:
            return '자유게시판'
        else:   # 정보 게시판이나 자유 게시판이 아닌 경우 기본으로 공지 게시판
            return '공지게시판'

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not (m[0][:2] == '__' or m[0] == 'name' or m[0] == 'value')]

        # format into django choice tuple
        choices = tuple([(p[1].value, BoardType(p[1]).get_title()) for p in props])

        return choices


# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200)                    # 글제목
    author = models.ForeignKey('auth.User')                     # 작성자
    created_date = models.DateTimeField(default=timezone.now)   # 작성일
    view_count = models.IntegerField(default=0)                 # 조회수
    text = models.TextField()                                   # 글내용
    type = models.CharField(u'게시판 종류', max_length=10, default='noti', choices=BoardType.choices())  # 소속 게시판

    def __str__(self):
        return self.title

    def article_viewed(self):
        self.view_count += 1
        self.save()

# =======
#
# # Create your models here.
#
# class InfoArticle(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     view_count = models.IntegerField(default = 0)
# >>>>>>> 8b1b4138db21c4cd23c12060e32a71ecd0e232a4
#
#     def __str__(self):
#         return self.title
#
# <<<<<<< HEAD
#     def article_viewed(self):
#         self.view_count += 1    # 글을 읽을 때 마다 조회수 + 1
#         self.save()
# =======
# class InfoComment(models.Model):
#     article = models.ForeignKey('board.InfoArticle', related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.text
#
# class CommentLikes(models.Model):
# 	user = models.ForeignKey('auth.User')
# 	comment = models.ForeignKey('board.InfoComment', related_name='likes')
# 	created_date = models.DateTimeField(default = timezone.now)
# >>>>>>> 8b1b4138db21c4cd23c12060e32a71ecd0e232a4
