# Generated by Django 4.2.7 on 2024-07-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0030_remove_packdownloads_pack_download_stages_completed_and_more'),
    ]

    operations = [

        migrations.AddField(
            model_name='stages',
            name='active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]