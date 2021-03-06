# Generated by Django 3.0.6 on 2020-07-09 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200708_2240'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matazim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='matazim/images/')),
                ('location', models.CharField(blank=True, max_length=50)),
                ('members', models.ManyToManyField(to='main.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='matazim/images/')),
                ('members', models.ManyToManyField(to='main.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('programs', models.ManyToManyField(to='matazim.Program')),
            ],
        ),
    ]
