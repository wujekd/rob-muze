# Generated by Django 4.1.13 on 2023-12-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0011_alter_vote_voter_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
