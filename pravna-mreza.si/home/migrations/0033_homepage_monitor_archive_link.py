# Generated by Django 3.1.14 on 2021-12-21 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
        ("home", "0032_auto_20211217_1204"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="monitor_archive_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Povezava do seznama monitoring zapisov",
            ),
        ),
    ]
