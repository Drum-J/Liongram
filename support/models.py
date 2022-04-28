from logging import PlaceHolder
from unicodedata import category
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class FAQ(models.Model) :
    일반 = '0'
    계정 = '1'
    기타 ='2'
    Category_choices = [
        (일반,'일반'),
        (계정,'계정'),
        (기타,'기타'),
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=Category_choices,
        default=일반
    )
    
    title = models.CharField(verbose_name='제목', max_length=50)
    content = models.TextField(verbose_name='내용')
    writer = models.ForeignKey(verbose_name='작성자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='writer_FAQ')
    modifier = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='modifier_FAQ')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    modify_date = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True)

class Inquiry(models.Model) :
    일반 = '0'
    계정 = '1'
    기타 ='2'
    Category_choices = [
        (일반,'일반'),
        (계정,'계정'),
        (기타,'기타'),
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=Category_choices,
        default=일반
    )

    title = models.CharField(verbose_name='제목', max_length=50)
    email = models.EmailField(verbose_name='이메일', blank=True)
    phone = models.CharField(verbose_name='문자메시지', max_length=11, blank=True)
    is_email = models.BooleanField(verbose_name='이메일 수신 여부', default=False)
    is_phone = models.BooleanField(verbose_name='문자메시지 수신 여부', default=False)
    content = models.TextField(verbose_name='문의 내용')
    image = models.ImageField(verbose_name='이미지',null=True, blank=True)
    writer = models.ForeignKey(verbose_name='작성자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='writer_inquiry')
    modifier = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='modifier_inquiry')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    modify_date = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True)

class Answer(models.Model):
    content = models.TextField(verbose_name='답변 내용')
    created_at = models.DateTimeField(verbose_name='답변 일시', auto_now_add=True)
    modify_date = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True)

    inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    writer = models.ForeignKey(verbose_name='작성자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='writer_answer')
    modifier = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='modifier_answer')