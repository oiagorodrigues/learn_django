# Generated by Django 5.1.2 on 2024-10-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("business_name", models.CharField(max_length=255)),
                ("document", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("street", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=20, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
