# Generated by Django 3.2.13 on 2022-06-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_titlee'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titleee',
            field=models.CharField(default='text', max_length=120),
        ),
    ]
