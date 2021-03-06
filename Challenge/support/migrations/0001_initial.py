# Generated by Django 4.0.4 on 2022-04-15 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('NO', '일반'), ('ID', '계정'), ('OT', '기타')], default='NO', max_length=2)),
                ('heading', models.TextField(verbose_name='제목')),
                ('email', models.TextField(verbose_name='이메일')),
                ('sms', models.TextField(verbose_name='문자메시지')),
                ('content', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답변 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('last_modified_at', models.DateTimeField(auto_now_add=True, verbose_name='최종 수정 일시')),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
                ('last_modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_modifier', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
