# Generated by Django 5.1.2 on 2024-10-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="document",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]