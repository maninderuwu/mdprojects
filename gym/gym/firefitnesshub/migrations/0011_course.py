# Generated by Django 4.2.5 on 2023-09-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firefitnesshub', '0010_alter_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='home')),
            ],
        ),
    ]