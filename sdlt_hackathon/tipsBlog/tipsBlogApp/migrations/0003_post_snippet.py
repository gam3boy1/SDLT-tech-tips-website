# Generated by Django 3.1 on 2021-03-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipsBlogApp', '0002_remove_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='', max_length=255),
        ),
    ]
