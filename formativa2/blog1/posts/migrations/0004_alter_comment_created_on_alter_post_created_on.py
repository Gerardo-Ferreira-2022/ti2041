# Generated by Django 4.2.7 on 2023-11-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]