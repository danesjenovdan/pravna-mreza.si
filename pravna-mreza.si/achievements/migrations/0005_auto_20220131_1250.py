# Generated by Django 3.1.14 on 2022-01-31 12:50

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0004_auto_20211226_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='link',
            field=wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani.', label='Ime', required=False)), ('page', wagtail.blocks.PageChooserBlock(label='Stran')), ('has_border', wagtail.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))])), ('external_link', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Ime')), ('url', wagtail.blocks.URLBlock(label='Povezava')), ('has_border', wagtail.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))])), ('email_link', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Ime')), ('email', wagtail.blocks.EmailBlock(label='Email povezava'))]))], null=True, verbose_name='Povezava'),
        ),
    ]
