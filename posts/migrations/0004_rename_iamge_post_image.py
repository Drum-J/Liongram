# Generated by Django 4.0.4 on 2022-05-04 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_image_post_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='iamge',
            new_name='image',
        ),
    ]