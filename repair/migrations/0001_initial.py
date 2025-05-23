# Generated by Django 5.1.6 on 2025-02-19 18:43

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=1500)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="MobileRepair",
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
                ("title", models.CharField(max_length=1500)),
                ("image", models.ImageField(upload_to="repair/images")),
                ("little_content", ckeditor_uploader.fields.RichTextUploadingField()),
                ("content", ckeditor_uploader.fields.RichTextUploadingField()),
                ("price", models.BigIntegerField()),
                ("status", models.BooleanField(default=True)),
                ("on_sale", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Comments",
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
                (
                    "message",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "mobile_repair",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to="repair.mobilerepair",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Repair",
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
                ("title", models.CharField(max_length=2500)),
                ("image", models.ImageField(upload_to="repair/images")),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="repair_category", to="repair.category"
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
        migrations.AddField(
            model_name="mobilerepair",
            name="repair",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mobile_repair",
                to="repair.repair",
            ),
        ),
    ]
