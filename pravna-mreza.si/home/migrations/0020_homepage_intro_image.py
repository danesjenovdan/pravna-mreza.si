# Generated by Django 3.1.10 on 2021-12-09 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0019_auto_20211209_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]