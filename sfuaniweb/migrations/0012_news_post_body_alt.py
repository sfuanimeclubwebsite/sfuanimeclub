# Generated by Django 3.0.5 on 2020-08-31 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuaniweb', '0011_auto_20200831_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='body_alt',
            field=models.CharField(help_text='Title of blog posting', max_length=255, null=True),
        ),
    ]
