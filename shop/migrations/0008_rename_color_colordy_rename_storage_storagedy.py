# Generated by Django 5.1.6 on 2025-06-14 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_remove_color_title_remove_product_color_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Color",
            new_name="ColorDy",
        ),
        migrations.RenameModel(
            old_name="Storage",
            new_name="StorageDy",
        ),
    ]
