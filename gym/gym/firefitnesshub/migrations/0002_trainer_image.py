# Generated by Django 4.2.4 on 2023-09-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firefitnesshub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
