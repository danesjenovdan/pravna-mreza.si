# Generated by Django 3.1.10 on 2021-12-09 22:03

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20211209_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationsettings',
            name='navigation_links',
            field=wagtail.fields.StreamField([('page_link', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani.', label='Ime', required=False)), ('page', wagtail.blocks.PageChooserBlock(label='Stran')), ('has_border', wagtail.blocks.BooleanBlock(label='Gumb ima obrobo?'))])), ('external_link', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Ime')), ('url', wagtail.blocks.URLBlock(label='Povezava')), ('has_border', wagtail.blocks.BooleanBlock(label='Gumb ima obrobo?'))]))], verbose_name='Povezave v glavi'),
        ),
    ]
