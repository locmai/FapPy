# Generated by Django 2.0.2 on 2018-02-18 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userkey',
            old_name='user',
            new_name='supervisor_user',
        ),
    ]
