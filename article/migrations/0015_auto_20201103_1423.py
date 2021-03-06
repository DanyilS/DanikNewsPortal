# Generated by Django 3.1.2 on 2020-11-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20201101_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Содержание'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
