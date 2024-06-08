# Generated by Django 4.2.7 on 2024-06-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0018_voting_description_en_voting_name_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collabsub',
            old_name='sprawdzone',
            new_name='approved',
        ),
        migrations.RemoveField(
            model_name='collabsub',
            name='odpowiedz',
        ),
        migrations.AddField(
            model_name='collabsub',
            name='checked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='collabsub',
            name='demoCreated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='collabsub',
            name='modComment',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
