# Generated by Django 5.0 on 2024-02-07 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tietle',
            new_name='title',
        ),
    ]
