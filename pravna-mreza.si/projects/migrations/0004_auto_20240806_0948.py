# Generated by Django 3.2 on 2024-08-06 09:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20240126_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='projectsarchivepage',
            name='projects',
            field=wagtail.fields.StreamField([('project', wagtail.blocks.StructBlock([('project', wagtail.blocks.PageChooserBlock(page_type=['projects.ProjectPage']))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
