# Generated by Django 3.1 on 2020-08-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200829_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
