# Generated by Django 2.2 on 2021-05-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
