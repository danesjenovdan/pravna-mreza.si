# Generated by Django 3.1.14 on 2022-01-31 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0005_auto_20220131_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='link_text',
        ),
    ]
