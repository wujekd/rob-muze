# Generated by Django 4.2.7 on 2024-05-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_alter_sampel_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampel',
            name='description_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sampel',
            name='title_en',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]