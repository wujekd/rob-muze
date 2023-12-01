# Generated by Django 4.1.10 on 2023-07-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sampel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mp3_file', models.FileField(upload_to='music/')),
                ('points_required', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='music/images/')),
                ('artist', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=150)),
            ],
        ),
    ]
