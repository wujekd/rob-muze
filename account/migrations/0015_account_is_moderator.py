# Generated by Django 4.2.7 on 2024-06-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_account_social1_alter_account_social2'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
    ]
