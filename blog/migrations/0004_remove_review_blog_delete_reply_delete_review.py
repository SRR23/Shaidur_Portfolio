# Generated by Django 5.0.7 on 2024-07-16 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_review_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
