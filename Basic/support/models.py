from enum import auto
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()

class Faq(models.Model):

    class Items(models.TextChoices):
        NORMAL = 'NO', _('일반')
        ID = 'ID', _('계정')
        OTHERS = 'OT', _('기타')

    question = models.TextField(verbose_name='질문')
    category = models.CharField(
        max_length=2,
        choices=Items.choices,
        default=Items.NORMAL,
    )
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='writer', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='last_modifier', null=True, blank=True)
    last_modified_at = models.DateTimeField(verbose_name='최종 수정일시', auto_now_add=True)
