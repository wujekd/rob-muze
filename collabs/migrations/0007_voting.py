# Generated by Django 4.1.10 on 2023-08-20 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0006_collab_glosowanie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('collab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabs.collab')),
            ],
        ),
    ]