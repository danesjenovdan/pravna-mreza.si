# Generated by Django 3.1.5 on 2021-01-27 11:03

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_auto_20210120_1014"),
    ]

    operations = [
        migrations.CreateModel(
            name="Infopush",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("text", wagtail.fields.RichTextField()),
            ],
        ),
    ]
