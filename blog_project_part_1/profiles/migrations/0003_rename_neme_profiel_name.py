# Generated by Django 5.0 on 2024-02-06 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiel_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiel',
            old_name='neme',
            new_name='name',
        ),
    ]
