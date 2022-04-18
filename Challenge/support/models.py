from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Inquiry(models.Model):
    
    class Items(models.TextChoices):
        NORMAL = 'NO', _('일반')
        ID = 'ID', _('계정')
        OTHERS = 'OT', _('기타')

    category = models.CharField(
        max_length=2, 
        choices=Items.choices, 
        default=Items.NORMAL, 
    )
    heading = models.TextField(verbose_name='제목')
    email = models.TextField(verbose_name='이메일')
    sms = models.TextField(verbose_name='문자메시지')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)


class Answer(models.Model):
    answer = models.TextField(verbose_name='답변 내용')
    inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='writer')
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    last_modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='last_modifier')
    last_modified_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now_add=True)
