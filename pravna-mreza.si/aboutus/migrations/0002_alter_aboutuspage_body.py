# Generated by Django 3.2 on 2024-08-06 09:48

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aboutus", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutuspage",
            name="body",
            field=wagtail.fields.StreamField(
                [("paragraph", wagtail.blocks.RichTextBlock())], use_json_field=True
            ),
        ),
    ]
