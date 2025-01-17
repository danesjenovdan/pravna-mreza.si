# Generated by Django 3.1.10 on 2021-12-09 16:49

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_navigationsettings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationsettings",
            name="navigation_links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "page_link",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        help_text="Če je prazno se uporabi naslov strani.",
                                        label="Ime",
                                        required=False,
                                    ),
                                ),
                                (
                                    "page",
                                    wagtail.blocks.PageChooserBlock(label="Stran"),
                                ),
                            ]
                        ),
                    ),
                    (
                        "external_link",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock(label="Ime")),
                                ("url", wagtail.blocks.URLBlock(label="Povezava")),
                            ]
                        ),
                    ),
                    ("has_border", wagtail.blocks.BooleanBlock()),
                ],
                verbose_name="Povezave v glavi",
            ),
        ),
    ]
