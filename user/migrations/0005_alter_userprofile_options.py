# Generated by Django 3.2.5 on 2022-05-05 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220427_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': True, 'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
