# Generated by Django 2.0.2 on 2018-02-18 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_in_charge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_manager_in_charge', to=settings.AUTH_USER_MODEL)),
                ('user_under_control', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_manager_under_control', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
