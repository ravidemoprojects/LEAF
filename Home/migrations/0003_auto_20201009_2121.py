# Generated by Django 3.1 on 2020-10-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20201009_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.URLField(max_length=5000),
        ),
    ]