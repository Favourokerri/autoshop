# Generated by Django 5.0.1 on 2024-01-27 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='css_class',
        ),
    ]
