# Generated by Django 4.2.5 on 2023-09-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firefitnesshub', '0007_trainer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(blank=True, upload_to='trainers_profile'),
        ),
    ]
