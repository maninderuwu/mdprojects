# Generated by Django 5.0.1 on 2024-01-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('md_cms', '0002_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
