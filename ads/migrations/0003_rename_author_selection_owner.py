# Generated by Django 4.2 on 2023-05-15 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='author',
            new_name='owner',
        ),
    ]