# Generated by Django 5.1.6 on 2025-06-14 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_rename_title_storage_storage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="storage",
            old_name="storage",
            new_name="title",
        ),
    ]
