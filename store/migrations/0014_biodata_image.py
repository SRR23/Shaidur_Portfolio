# Generated by Django 5.0.7 on 2024-07-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_biodata'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='image',
            field=models.ImageField(default='', upload_to='profile_image'),
        ),
    ]
