# Generated by Django 4.2.2 on 2023-06-30 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryValue',
            new_name='Specifications',
        ),
    ]
