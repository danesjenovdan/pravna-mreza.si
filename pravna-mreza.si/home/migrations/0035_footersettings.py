# Generated by Django 3.1.14 on 2021-12-22 11:09

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0034_auto_20211222_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_text', models.TextField(blank=True, verbose_name='Besedilo v footerju')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook URL')),
                ('twitter_link', models.URLField(blank=True, null=True, verbose_name='Twitter URL')),
                ('footer_links_left', wagtail.core.fields.StreamField([('page_link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani.', label='Ime', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran')), ('has_border', wagtail.core.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))])), ('external_link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(label='Ime')), ('url', wagtail.core.blocks.URLBlock(label='Povezava')), ('has_border', wagtail.core.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))]))], verbose_name='Povezave v nogi na levi')),
                ('footer_links_right', wagtail.core.fields.StreamField([('page_link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Če je prazno se uporabi naslov strani.', label='Ime', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran')), ('has_border', wagtail.core.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))])), ('external_link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(label='Ime')), ('url', wagtail.core.blocks.URLBlock(label='Povezava')), ('has_border', wagtail.core.blocks.BooleanBlock(label='Gumb ima obrobo?', required=False))]))], verbose_name='Povezave v nogi na desni')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
    ]