# Generated by Django 3.1.4 on 2021-01-04 18:10

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('part_one', wagtail.core.blocks.CharBlock(required=False)), ('part_two', wagtail.core.blocks.CharBlock(required=False)), ('intro_text', wagtail.core.blocks.RichTextBlock(required=False))], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())]),
        ),
    ]
