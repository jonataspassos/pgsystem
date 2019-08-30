# Generated by Django 2.2.4 on 2019-08-30 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ManyToManyField(related_name='Children', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PequenoGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='PG MyStyle', max_length=30, verbose_name='PG Name')),
                ('leader', models.ManyToManyField(related_name='leader', to=settings.AUTH_USER_MODEL)),
                ('participant', models.ManyToManyField(related_name='participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
