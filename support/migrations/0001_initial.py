# Generated by Django 4.0.4 on 2022-04-28 08:01

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
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('0', '일반'), ('1', '계정'), ('2', '기타')], default='0', max_length=2, verbose_name='카테고리')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='최종 수정일시')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modifier_FAQ', to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer_FAQ', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]