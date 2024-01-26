# Generated by Django 3.1.14 on 2024-01-26 12:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectsarchivepage_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsarchivepage',
            name='projects',
            field=wagtail.core.fields.StreamField([('project', wagtail.core.blocks.StructBlock([('project', wagtail.core.blocks.PageChooserBlock(page_type=['projects.ProjectPage']))]))], blank=True, null=True),
        ),
    ]
