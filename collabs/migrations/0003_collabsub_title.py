# Generated by Django 4.1.10 on 2023-08-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0002_collab_download_pack_collabsub_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='collabsub',
            name='title',
            field=models.TextField(max_length=40, null=True),
        ),
    ]
