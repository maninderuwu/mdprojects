# Generated by Django 4.2.4 on 2023-09-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firefitnesshub', '0003_delete_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duration', models.PositiveIntegerField(help_text='duration on the basis of months')),
            ],
        ),
        migrations.DeleteModel(
            name='Gymclass',
        ),
    ]
