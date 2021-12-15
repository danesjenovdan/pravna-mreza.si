# Generated by Django 3.1.10 on 2021-12-10 14:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0021_infopush_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopush',
            name='page_text',
            field=models.TextField(blank=True, null=True, verbose_name='Besedilo na gumbu s povezavo (neobvezno)'),
        ),
        migrations.AlterField(
            model_name='infopush',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Povezava do strani (neobvezno)'),
        ),
        migrations.AlterField(
            model_name='infopush',
            name='text',
            field=wagtail.core.fields.RichTextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='infopush',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Naslov (neobvezno)'),
        ),
    ]