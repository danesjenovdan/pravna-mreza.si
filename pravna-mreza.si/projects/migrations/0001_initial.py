# Generated by Django 3.1.14 on 2023-05-09 09:33

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectsArchivePage",
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
                "verbose_name": "Seznam projektov",
                "verbose_name_plural": "Seznami projektov",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ProjectPage",
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
                ("preview_text", wagtail.fields.RichTextField(default="")),
                (
                    "intro_text",
                    wagtail.fields.RichTextField(
                        blank=True, null=True, verbose_name="Opis"
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [("paragraph", wagtail.blocks.RichTextBlock())]
                    ),
                ),
                (
                    "meta_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="OG slika",
                    ),
                ),
                (
                    "preview_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Projekt",
                "verbose_name_plural": "Projekti",
            },
            bases=("wagtailcore.page",),
        ),
    ]
