# Generated by Django 4.1.13 on 2023-12-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_account_vocals'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='instrument',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='mixmaster',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='production',
            field=models.BooleanField(default=False),
        ),
    ]
