# Generated by Django 5.0 on 2024-02-06 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('profiles', '0003_rename_neme_profiel_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profiel',
            new_name='Profile',
        ),
    ]
