# Generated by Django 2.2.4 on 2019-08-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pequenogrupo',
            name='name',
            field=models.CharField(default='PG MyStyle', max_length=30, verbose_name='Nome do PG'),
        ),
    ]