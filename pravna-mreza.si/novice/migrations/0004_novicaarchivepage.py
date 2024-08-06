# Generated by Django 3.1.5 on 2021-02-25 11:30

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('novice', '0003_novicapage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovicaArchivePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('part_one', wagtail.blocks.CharBlock(required=False)), ('part_two', wagtail.blocks.CharBlock(required=False))], icon='title'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
