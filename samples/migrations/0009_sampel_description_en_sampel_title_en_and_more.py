# Generated by Django 4.1.13 on 2024-01-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0008_alter_sampel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampel',
            name='description_en',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sampel',
            name='title_en',
            field=models.CharField(default='test', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sampel',
            name='title',
            field=models.CharField(default='test', max_length=200, null=True),
        ),
    ]