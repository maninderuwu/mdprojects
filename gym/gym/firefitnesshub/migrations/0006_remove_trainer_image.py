# Generated by Django 4.2.5 on 2023-09-06 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firefitnesshub', '0005_delete_membership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='image',
        ),
    ]
