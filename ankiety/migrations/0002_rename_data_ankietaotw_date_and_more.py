# Generated by Django 4.2.7 on 2024-05-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankiety', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ankietaotw',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='ankietaotw',
            old_name='pytanie',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='ankietaotw',
            old_name='kategoria',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='ankietaotw',
            old_name='tytol',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='odpowiedzotw',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='odpowiedzotw',
            old_name='ankietaotw',
            new_name='poll',
        ),
        migrations.AddField(
            model_name='ankietaotw',
            name='question_en',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='ankietaotw',
            name='title_en',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='odpowiedzotw',
            name='answer_en',
            field=models.TextField(blank=True, max_length=700),
        ),
    ]
