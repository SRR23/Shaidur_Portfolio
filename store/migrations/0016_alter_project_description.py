# Generated by Django 5.0.7 on 2024-07-17 09:25

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_biodata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
