# Generated by Django 3.1.14 on 2022-02-22 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20220222_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthorrelationship',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.author', verbose_name='Avtor_ica'),
        ),
    ]