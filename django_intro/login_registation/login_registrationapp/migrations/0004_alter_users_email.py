# Generated by Django 3.2.1 on 2021-06-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registrationapp', '0003_auto_20210528_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
