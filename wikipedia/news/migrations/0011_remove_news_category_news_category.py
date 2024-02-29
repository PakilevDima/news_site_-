# Generated by Django 4.2.10 on 2024-02-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_rename_body_news_content_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(to='news.category'),
        ),
    ]
