# Generated by Django 3.1.14 on 2021-12-26 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_blogpage_meta_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogarchivepage",
            options={
                "verbose_name": "Seznam blog zapisov",
                "verbose_name_plural": "Seznam blog zapisov",
            },
        ),
        migrations.AlterModelOptions(
            name="blogpage",
            options={"verbose_name": "Blog", "verbose_name_plural": "Blog"},
        ),
    ]
