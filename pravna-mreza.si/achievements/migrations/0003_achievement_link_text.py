# Generated by Django 3.1.14 on 2021-12-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0002_auto_20211221_1319"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="link_text",
            field=models.TextField(blank=True, verbose_name="Besedilo na gumbu"),
        ),
    ]
