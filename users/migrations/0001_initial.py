# Generated by Django 2.2.4 on 2019-08-25 17:00

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nickname', models.CharField(max_length=30, unique=True, verbose_name='NickName')),
                ('username', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^((?P<postal>\\+?\\d{2,3})?[ -]*(?P<ddd>(\\(\\d{2}\\))|\\d{2}))?[ -]*(?P<num1>\\d{4,5})[ -]*(?P<num2>\\d{4})$'), 'Phone not recognized', 'invalid')], verbose_name='Phone')),
                ('image', models.TextField(blank=True, verbose_name='Avatar')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Administrator')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
