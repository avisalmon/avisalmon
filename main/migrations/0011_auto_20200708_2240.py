# Generated by Django 3.0.6 on 2020-07-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200622_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fake',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='mataz',
            field=models.BooleanField(default=False),
        ),
    ]