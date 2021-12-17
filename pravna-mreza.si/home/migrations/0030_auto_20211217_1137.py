# Generated by Django 3.1.14 on 2021-12-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0029_auto_20211217_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Družbena omrežja'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_failure',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_success',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_terms',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_title_part_one',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='newsletter_title_part_two',
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='social_media_title_part_one',
            field=models.TextField(blank=True, verbose_name='Škatla družbena omrežja - naslov 1. del'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='social_media_title_part_two',
            field=models.TextField(blank=True, verbose_name='Škatla družbena omrežja - naslov 2. del'),
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_title_part_one', models.TextField(blank=True, verbose_name='Škatla novičnik - naslov 1. del')),
                ('newsletter_title_part_two', models.TextField(blank=True, verbose_name='Škatla novičnik - naslov 2. del')),
                ('newsletter_terms', models.TextField(blank=True, verbose_name='Škatla novičnik - pogoji')),
                ('newsletter_success', models.TextField(blank=True, verbose_name='Škatla novičnik - sporočilo ob uspešni prijavi')),
                ('newsletter_failure', models.TextField(blank=True, verbose_name='Škatla novičnik - sporočilo ob neuspešni prijavi')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Novičnik',
            },
        ),
    ]
