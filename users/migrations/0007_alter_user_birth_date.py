# Generated by Django 4.2 on 2023-05-18 21:22

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[users.validators.checkBDay]),
        ),
    ]
