# Generated by Django 5.1.6 on 2025-06-14 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_rename_color_colordy_rename_storage_storagedy"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StorageDy",
            new_name="Storage",
        ),
        migrations.RenameField(
            model_name="storage",
            old_name="storage",
            new_name="title",
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=2500, null=True)),
                ("price", models.BigIntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_color",
                        to="shop.product",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ColorDy",
        ),
    ]
