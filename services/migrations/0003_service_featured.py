# Generated by Django 5.0.1 on 2024-01-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_icon_css_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='featured',
            field=models.BooleanField(default=False, help_text='mark to display in home page'),
        ),
    ]
