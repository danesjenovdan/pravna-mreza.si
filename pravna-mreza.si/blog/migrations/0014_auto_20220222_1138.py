# Generated by Django 3.1.14 on 2022-02-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_auto_20211226_2136"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpage",
            name="author",
        ),
        migrations.AddField(
            model_name="blogpage",
            name="authors",
            field=models.ManyToManyField(
                blank=True, null=True, to="blog.Author", verbose_name="Avtor"
            ),
        ),
    ]
