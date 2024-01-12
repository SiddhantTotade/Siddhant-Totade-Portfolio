# Generated by Django 5.0.1 on 2024-01-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("description", models.TextField()),
                ("github", models.URLField(blank=True, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("resume", models.FileField(blank=True, null=True, upload_to="media")),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField()),
                ("github", models.URLField(blank=True, null=True)),
                ("live", models.URLField(blank=True, null=True)),
                ("is_live", models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("skill_name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "skill_logo",
                    models.ImageField(blank=True, null=True, upload_to="media"),
                ),
            ],
        ),
    ]
