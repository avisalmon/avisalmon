# Generated by Django 3.0.6 on 2020-06-23 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presenterz', '0004_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='presenterz.Lecture'),
        ),
    ]
