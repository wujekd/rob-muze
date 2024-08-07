# Generated by Django 4.2.7 on 2024-07-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0025_alter_voting_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('name_pl', models.CharField(max_length=35)),
                ('desc', models.TextField(max_length=200)),
                ('desc_pl', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=50)),
                ('download_pack', models.FileField(blank=True, null=True, upload_to='collabs/downloads')),
                ('backing_track', models.FileField(blank=True, null=True, upload_to='collabs/demos')),
                ('demo', models.BooleanField(default=False)),
                ('score', models.BooleanField(default=False)),
                ('midi', models.BooleanField(default=False)),
                ('ableton', models.BooleanField(default=False)),
                ('reaper', models.BooleanField(default=False)),
                ('logic', models.BooleanField(default=False)),
                ('wokal', models.BooleanField(default=False)),
                ('instrument', models.BooleanField(default=False)),
                ('rap', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='collab',
            name='ableton',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='backing_track',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='demo',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='download_pack',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='logic',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='midi',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='rap',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='reaper',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='score',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='votingActive',
        ),
        migrations.RemoveField(
            model_name='collab',
            name='wokal',
        ),
        migrations.RemoveField(
            model_name='collabsub',
            name='collab',
        ),
        migrations.RemoveField(
            model_name='packdownloads',
            name='collab',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voting',
        ),
        migrations.DeleteModel(
            name='Voting',
        ),
        migrations.AddField(
            model_name='stages',
            name='collab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabs.collab'),
        ),
        migrations.AddField(
            model_name='collabsub',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='collabs.stages'),
        ),
        migrations.AddField(
            model_name='packdownloads',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collabs.stages'),
        ),
        migrations.AddField(
            model_name='vote',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collabs.stages'),
        ),
    ]
