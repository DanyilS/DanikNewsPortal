# Generated by Django 3.1.2 on 2020-11-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20201103_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=0, upload_to='profile_photos'),
            preserve_default=False,
        ),
    ]
