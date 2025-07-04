# Generated by Django 5.1.6 on 2025-04-11 15:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0004_remove_product_color_remove_product_region_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscountCode",
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
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="نام کد تخفیف"
                    ),
                ),
                (
                    "discount",
                    models.SmallIntegerField(default=0, verbose_name="مقدار درصد تفیف"),
                ),
                (
                    "quantity",
                    models.SmallIntegerField(default=1, verbose_name="تعداد کد تخفیف"),
                ),
            ],
            options={
                "verbose_name": "کد تخفیف",
                "verbose_name_plural": "تنظیمات قسمت  کد های تخفیف",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                    "total_price",
                    models.IntegerField(default=0, verbose_name="قیمت کلی"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "is_pay",
                    models.BooleanField(
                        default=False, verbose_name="ایا پرداخت شده است ؟"
                    ),
                ),
                (
                    "addresses",
                    models.TextField(blank=True, null=True, verbose_name="آدرس کاربر"),
                ),
                (
                    "image_payed",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="pay/image",
                        verbose_name="عکس پرداخت موفق",
                    ),
                ),
                (
                    "DeliveryDate",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="تاریخ تحویل محصول"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_product",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "ثبت درخواست خرید",
                "verbose_name_plural": "تنظیمات قسمت ثبت درخواست خرید ها",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.SmallIntegerField(verbose_name="تعداد")),
                ("price", models.PositiveIntegerField(verbose_name="قیمت")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.order",
                        verbose_name="کالا درحال انجام",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="shop.product",
                        verbose_name="کالا",
                    ),
                ),
            ],
            options={
                "verbose_name": "پایان ثبت درخواست خرید",
                "verbose_name_plural": "تنظیمات قسمت  پایان ثبت درخواست خرید ها",
            },
        ),
    ]
