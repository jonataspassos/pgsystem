# Generated by Django 2.2.4 on 2019-08-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_userresponse_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='end',
            field=models.DateField(null=True),
        ),
    ]
