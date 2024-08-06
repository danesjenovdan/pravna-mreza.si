# Generated by Django 3.1.4 on 2021-01-04 18:10

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('part_one', wagtail.blocks.CharBlock(required=False)), ('part_two', wagtail.blocks.CharBlock(required=False)), ('intro_text', wagtail.blocks.RichTextBlock(required=False))], icon='title')), ('paragraph', wagtail.blocks.RichTextBlock())]),
        ),
    ]
