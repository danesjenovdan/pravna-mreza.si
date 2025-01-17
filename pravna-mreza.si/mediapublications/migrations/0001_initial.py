# Generated by Django 3.1.14 on 2021-12-24 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
    ]

    operations = [
        migrations.CreateModel(
            name="MediaPublicationsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "headline_first",
                    models.TextField(blank=True, verbose_name="Naslovnica prvi del"),
                ),
                (
                    "headline_second",
                    models.TextField(blank=True, verbose_name="Naslovnica drugi del"),
                ),
                (
                    "headline_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Slika na naslovnici",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
