# Generated by Django 3.2.1 on 2021-05-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registrationapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='users',
            name='firstname',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
    ]
