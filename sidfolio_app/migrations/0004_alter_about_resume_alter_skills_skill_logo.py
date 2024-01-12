# Generated by Django 5.0.1 on 2024-01-09 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sidfolio_app", "0003_alter_skills_skill_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="skills",
            name="skill_logo",
            field=models.FileField(
                default="none",
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(["pdf", "doc", "svg"])
                ],
            ),
        ),
    ]
