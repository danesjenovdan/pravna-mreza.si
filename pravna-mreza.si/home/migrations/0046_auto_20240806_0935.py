# Generated by Django 3.2 on 2024-08-06 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0045_auto_20230220_2250"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="footersettings",
            name="site",
        ),
        migrations.RemoveField(
            model_name="monitor",
            name="site",
        ),
        migrations.RemoveField(
            model_name="navigationsettings",
            name="site",
        ),
        migrations.RemoveField(
            model_name="newsletter",
            name="site",
        ),
        migrations.RemoveField(
            model_name="ogsettings",
            name="site",
        ),
        migrations.RemoveField(
            model_name="socialmedia",
            name="site",
        ),
        migrations.RemoveField(
            model_name="support",
            name="site",
        ),
    ]
