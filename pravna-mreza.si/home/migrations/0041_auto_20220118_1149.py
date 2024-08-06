# Generated by Django 3.1.14 on 2022-01-18 11:49

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20220117_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='monitor_box',
            field=models.BooleanField(default=False, verbose_name='Škatla prispevaj'),
        ),
        migrations.AddField(
            model_name='genericpage',
            name='newsletter_box',
            field=models.BooleanField(default=False, verbose_name='Škatla novičnik'),
        ),
        migrations.AddField(
            model_name='genericpage',
            name='social_media_box',
            field=models.BooleanField(default=False, verbose_name='Škatla družbena omrežja'),
        ),
        migrations.AddField(
            model_name='genericpage',
            name='support_box',
            field=models.BooleanField(default=False, verbose_name='Škatla podpri'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())]),
        ),
    ]
