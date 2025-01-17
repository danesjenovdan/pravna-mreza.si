# Generated by Django 3.2 on 2024-08-06 09:48

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_auto_20220222_1721"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("paragraph", wagtail.blocks.RichTextBlock())],
                use_json_field=True,
                verbose_name="Besedilo",
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="related_blog_posts",
            field=wagtail.fields.StreamField(
                [
                    (
                        "blog_post",
                        wagtail.blocks.PageChooserBlock(
                            label="Povezava do blog zapisa"
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Povezani blog zapisi",
            ),
        ),
    ]
