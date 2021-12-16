# Generated by Django 3.1.14 on 2021-12-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20211215_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_button',
        ),
        migrations.AddField(
            model_name='homepage',
            name='newsletter_failure',
            field=models.TextField(blank=True, default='', verbose_name='Škatla novičnik - sporočilo ob neuspešni prijavi'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='newsletter_success',
            field=models.TextField(blank=True, default='', verbose_name='Škatla novičnik - sporočilo ob uspešni prijavi'),
        ),
    ]