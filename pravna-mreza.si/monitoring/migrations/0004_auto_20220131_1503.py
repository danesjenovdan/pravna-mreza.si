# Generated by Django 3.1.14 on 2022-01-31 15:03

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("monitoring", "0003_auto_20211226_2136"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="monitoringarchivepage",
            name="get_in_touch",
        ),
        migrations.RemoveField(
            model_name="monitoringarchivepage",
            name="get_in_touch_text",
        ),
        migrations.AddField(
            model_name="monitoringarchivepage",
            name="link",
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
                                (
                                    "has_border",
                                    wagtail.blocks.BooleanBlock(
                                        label="Gumb ima obrobo?", required=False
                                    ),
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
                                (
                                    "has_border",
                                    wagtail.blocks.BooleanBlock(
                                        label="Gumb ima obrobo?", required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "email_link",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock(label="Ime")),
                                (
                                    "email",
                                    wagtail.blocks.EmailBlock(label="Email povezava"),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Povezava v opisu",
            ),
        ),
    ]
