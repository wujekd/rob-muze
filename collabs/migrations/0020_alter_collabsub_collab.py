# Generated by Django 4.2.7 on 2024-06-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0019_rename_sprawdzone_collabsub_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collabsub',
            name='collab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='collabs.collab'),
        ),
    ]
