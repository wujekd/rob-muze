# Generated by Django 4.1.10 on 2023-07-28 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_sampel_cena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampel',
            name='points_required',
        ),
    ]
