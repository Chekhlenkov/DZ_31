# Generated by Django 4.2 on 2023-05-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_managers_user_date_joined_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
