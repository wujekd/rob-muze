# Generated by Django 4.2.7 on 2024-06-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0020_alter_collabsub_collab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collab',
            old_name='glosowanie',
            new_name='votingActive',
        ),
        migrations.AddField(
            model_name='collab',
            name='pic',
            field=models.FileField(null=True, upload_to='collabs/demos'),
        ),
        migrations.AlterField(
            model_name='collab',
            name='backing_track',
            field=models.FileField(blank=True, null=True, upload_to='collabs/demos'),
        ),
        migrations.AlterField(
            model_name='collabsub',
            name='file',
            field=models.FileField(null=True, upload_to='collabs/responses'),
        ),
    ]
