# Generated by Django 4.1.13 on 2023-12-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profesja',
        ),
        migrations.AddField(
            model_name='account',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/images/'),
        ),
    ]
